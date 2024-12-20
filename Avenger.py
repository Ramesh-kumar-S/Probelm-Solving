#!/users/rameseka/python2.7/bin/python2.7
from __future__ import print_function
import urllib2
import xml.etree.ElementTree as ET
import json
import os
import stat
import sys
import argparse
import textwrap
from multiprocessing import Pool, Lock, Manager
from functools import partial
import logging

#Multiple Domain Inventory (Multithreading) -- Done
#Search through all Domains  -- Done
#Implement Server ID Attribute for all Components -- DONE
#Implement CLI Based Mechanism - Done
#Setup Addition and  Deletion Mechanism  -- Done
#Check if the setup is up or not - Done
#Add Update domain Functionality
#Handle Urllib Error -- Done

Result={}
SearchQuery=""


def scriptLogging():
    """
         Function Initializes a Logger Class
    """
    log_file_path = 'InventoryEngine.log'
    with open(log_file_path, 'w'):
        pass
    os.chmod(log_file_path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
    
    logging.basicConfig(
    filename=log_file_path,
    level=logging.DEBUG,
    format="%(asctime)s: %(filename)s: %(funcName)s: %(lineno)s:  %(levelname)s:  %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S',
    filemode='w'
    )
    logger = logging.getLogger() 
    return logger

def log(message):
    logging.info(message)
      
def Welcome():
    Ret_Val =os.system('clear')
    print(140*"-")
    print("Inventory Management Engine V1.1".center(140))
    print(140*"-")
    scriptLogging()
    log("Entering the Inventory Management Engine")
    print("\nHang on for a second... Processing\n")
    
    
#Add, Update, Delete (CRUD)
def addDomain(IP, username, Password):
    """
         Add's a New Domain to the Config Json File
    """
    if os.path.exists("Config.json"):
        try:
            with open("Config.json","r") as f:
                f.seek(0)
                ExistingData=json.load(f)
        except ValueError:
            ExistingData = {}
            
        with open("Config.json","r+") as f:
            if IP in ExistingData:
                print("\nData Already Exists")
                print("\nPlease proceed for the Query\n")
            else:
                ExistingData[IP]={IP: [IP, username, Password]}
                json.dump(ExistingData,f, indent=4)
                print("\nData updated Successfully")
    else:
        print("\nConfig File doesn't exists, Creating one")
        log("Config File doesn't exists, Creating one")
        with open("Config.json","w+") as f:
            f.seek(0)
            NewData={}
            NewData[IP]={IP: [IP, username, Password]}
            json.dump(NewData,f, indent=4)
            print("\nData updated Successfully\n")

def getDomain(DisplayOnConsole=False):
    """
         Fetches domain's from the Config Json File
    """
    if os.path.exists("Config.json"):
        if os.path.getsize("Config.json") == 0:
            print("Config file is empty. Nothing to fetch.\n")
            return
    else:
        print("Config file doesn't exist. Nothing to fetch.")
        return
            
    domains=[]
    try:
        with open("Config.json","r") as f:
            f.seek(0)
            Data=json.load(f)
            if DisplayOnConsole:
                print(json.dumps(Data, indent=4))
                print(140*"-")
            else:
                for value in Data.values():
                    toString=list(map(str, *value.values())) #Add Setup Up Check here 
                    HOST_UP=os.system("ping -c 1 {} >/dev/null".format(toString[0])) == 0
                    if not HOST_UP:
                        print("\nSkipping the Inventory on {} domain, As it's un-reachable.\n".format(toString[0]))
                        continue
                    domains.append(toString)
                log("Configured Domain's : {}".format(domains))
                if not domains:
                    print("\nConfig File is Empty, can't proceed further")
                    print("\nPlease add the Setup Info to proceed Further..Aborting")
                    sys.exit(0)
                return domains
    except IOError:
        print("Config File doesn't Exist's! Please add the add the setup Info using [ python <script> --add <SetupIP> <username> <password> ]\n")
        log("Config File doesn't Exist's!")
        sys.exit(0)
                

def removeDomain(IP):
    """
         Removes domain from the Config Json File
    """
    if os.path.exists("Config.json"):
        with open("Config.json","r") as f:
            f.seek(0)
            Data=json.load(f)
            if IP in Data:
                print("\nData found in config file, Removing the entry")
                del Data[IP]
    
                with open("Config.json","w") as f:
                    f.seek(0)
                    json.dump(Data,f, indent=4)
                    print("\nEntry Removed Successfully\n")
            else:
                print("\nEntry doesn't Exist, Nothing to delete, Aborting")
                print("\nPlease Ensure that Entry Exists in Config File by Feching via <Script> <getDomain> Command")
    else:
        print("\nConfig File doesn't exists in this Path, Nothing to Delete\n")
    
    
def FetchInventory(data,result):
    """_summary_

    Args:
        data (_list_): Data - [SetupIP, userName, passWord]
        result (_type_): Common Dictionary Across all the threads

    Returns:
        _dict_: Appends the Response to the result dict.
    """
    domainIP=data[0]
    userName=data[1]
    passWord=data[2]
    log("Entering the FetchInventory , IP : {}, Username : {}, Password : {}".format(domainIP, userName, passWord))
    
    #Handle URLib Error Exception and Return a Error code
    #Based on that Handle on the caller
    def sendConfigtoDme(payload):
        """_summary_

        Args:
            payload (str): XML String Payload

        Returns:
            Str: XML Response String Payload 
        """
        url="https://"+ domainIP + "/nuova"
        data=payload
        try:
            log("Request : {}\n".format(data))
            req=urllib2.Request(url=url, data=data, headers={'Content-Type': 'application/xml'})
            resp = urllib2.urlopen(req)
            xml_response = resp.read()
            log("Response : {}\n".format(xml_response))
            resp.close()
            return xml_response
        except urllib2.URLError as e:
            print("{} - Setup is not reachable from Build Machine, Please Verify the IP & Credentials\n".format(domainIP))
            return None
        except urllib2.HTTPError as e:
            print("{} - Setup is not reachable from Build Machine, Please Verify the IP & Credentials\n".format(domainIP))
            return None

    def getCookie():
        """ Fetches the cookie for the specific setup

        Returns:
            str:  Cookie
        """
        data="<aaaLogin inName=\"{}\" inPassword=\"{}\"/>".format(userName,passWord)
        Response=sendConfigtoDme(data)
        log("Received Response for {} : {}".format(domainIP, Response))
        if not Response:
            return
        root = ET.fromstring(Response)
        Response_Cookie = root.get('outCookie')
        # print("Fetched Cookie of {} : {}\n".format(domainIP, Response_Cookie))
        log("Fetched Cookie of {} : {}\n".format(domainIP, Response_Cookie))
        return Response_Cookie

    global Cookie
    Cookie=getCookie()
    if Cookie is None:
        return

    #Log out of the session
    def Logout():
        LogOut_Req="<aaaLogout inCookie=\""+Cookie+"\"/>"
        log("Logging out of {}".format(domainIP))
        sendConfigtoDme(LogOut_Req)

    def parseComputeRackUnitResponse(root):
        RACKS={}
        
        log("Parsing the Compute Rack Unit Response")
        for top in root.findall('.//outConfigs/*'):
            if top.tag == "computeRackUnit":
                RACKS[top.get('serial')] = {
                                                "Setup IP" : domainIP,
                                                "Server ID" : top.get('serverId'),
                                                "Server Type" : "Rack Server",
                                                "Server Model" : top.get('model'),
                                                "Server Serial" : top.get('serial'),
                                                "Discovery Status" : top.get('discovery'),
                                                "Managing Instance" : top.get('managingInst'),
                                                "No of Adapters Present" : top.get('numOfAdaptors')
                                            }
        result[str(domainIP)] = RACKS
  
    def parseComputeBladeResponse(root):
        BLADES={}
        
        log("Parsing the Compute Blade Response")
        for top in root.findall('.//outConfigs/*'):
            if top.tag == "computeBlade":
                BLADES[top.get('serial')] = {
                                                "Setup IP" : domainIP,
                                                "Chassis ID" : top.get('chassisId'),
                                                "Blade ID" : top.get('serverId'),
                                                "Server Type" : "Blade Server",
                                                "Server Model" : top.get('model'),
                                                "Server Serial" : top.get('serial'),
                                                "Discovery Status" : top.get('discovery'),
                                                "Managing Instance" : top.get('managingInst'),
                                                "No of Adapters Present" : top.get('numOfAdaptors')
                                            }
        result[str(domainIP)] = BLADES

    def parseAdapterUnitResponse(root):
        ADAPTERS={}
        
        log("Parsing the Adaptor Unit Response")
        for top in root.findall('.//outConfigs/*'):
            for child in top.findall('.//adaptorUnit'):
                if child.tag == "adaptorUnit":
                    ADAPTERS[child.get('serial')] = {
                                                    "Setup IP" : domainIP,
                                                    "Server ID" : top.get('serverId'),
                                                    "Adapter ID" : child.get('id'),
                                                    "Connectionn Path" : child.get('connPath'),
                                                    "Connection Status" : child.get('connStatus'),
                                                    "Adapter Model" : child.get('model'),
                                                    "Adapter Serial" : child.get('serial'),
                                                    "Adapter Vendor" : child.get('vendor')
                                                    }
        result[str(domainIP)] = ADAPTERS

    def parseControllerResponse(root):
        STORAGE_CONTROLLERS={}
        
        log("Parsing the Storage Controller Response")
        for top in root.findall(".//outConfigs/*"):
            for child in top.findall('.//computeBoard/storageController'):
                disks=[disk for disk in child.findall('.//storageLocalDisk')]
                if child.tag == "storageController":
                    STORAGE_CONTROLLERS[child.get('serial')] = {
                                                    "Setup IP" : domainIP,
                                                    "Server ID" : top.get('serverId'),
                                                    "Controller ID" : child.get('id'),
                                                    "Controller Type" : child.get('type'),
                                                    "Controller Model" : child.get('model'),
                                                    "Controller Serial" : child.get('serial'),
                                                    "Controller Vendor" : child.get('vendor'),
                                                    "Controller Security Flag":child.attrib['controllerFlags'],
                                                    "No of Disks Present":str(len(disks))
                                                    }
        result[str(domainIP)] = STORAGE_CONTROLLERS

    def parsestorageDiskResponse(root):
        STORAGE_LOCAL_DISKS={}
        
        log("Parsing the Storage Local Disk Response")
        for top in root.findall(".//outConfigs/*"):
            for child in top.findall('.//computeBoard/storageController/storageLocalDisk'):
                if child.tag == "storageLocalDisk":
                    STORAGE_LOCAL_DISKS[child.get('serial')] = {
                                                    "Setup IP" : domainIP,
                                                    "Server ID" : top.get('serverId'),
                                                    "Disk ID" : child.get('id'),
                                                    "Disk Type" : child.get('deviceType'),
                                                    "Disk Protocol" : child.get('connectionProtocol'),
                                                    "Disk State" : child.get('diskState'),
                                                    "Disk Model" : child.get('model'),
                                                    "Disk Serial" : child.get('serial'),
                                                    "Disk Vendor" : child.get('vendor')
                                                    }
        result[str(domainIP)] = STORAGE_LOCAL_DISKS
        
    def fetchCommonComponents():
        data="<configResolveClasses cookie=\""+Cookie+"\"inHierarchical=\"true\"> <inIds> <Id value=\"computeItem\"/> </inIds> </configResolveClasses>"
        Response=sendConfigtoDme(data)
        root = ET.fromstring(Response)
        
        if Component == "rack":
            parseComputeRackUnitResponse(root)
        elif Component == "blade":
            parseComputeBladeResponse(root)
        elif Component == "adapter":
            parseAdapterUnitResponse(root)
        elif Component == "controller":
            parseControllerResponse(root)
        elif Component == "disk":
            parsestorageDiskResponse(root)
    
    fetchCommonComponents()
    Logout()
    
        
def Main():
    """
       All the Domains will be Queries and Response will be stored
       in a common dictionary across all the threads
    Returns:
        dict : QueryResponse  will hold the response fetched across all the domains
    """
    Domains=getDomain()
    pool = Pool(processes=len(Domains))
    manager = Manager()
    R=manager.dict()
    pool.map(partial(FetchInventory, result=R), Domains)
    pool.close()
    pool.join()
    QueryResponse=R
    return QueryResponse
    
    
def RetrieveQueryfromGlobalJsonResult():
    """
    Searches for a Query on the Global Response
    """
    Query=dict(Main())
    if Query is not None:
        log("Searching for an {} in Global Response".format(SearchQuery))
        for SetupIP, Contents in Query.items():
            for S_No, CompContents in Contents.items():
                if not SearchQuery:
                    log("Dumping all the Inventory Data : {}".format(json.dumps(CompContents, indent=4)))
                    print(json.dumps(CompContents, indent=4))
                else:
                    for Value in CompContents.values():
                        if SearchQuery.lower() in Value.lower():
                            log("Search Response : {}".format(json.dumps(CompContents, indent=4)))
                            print(json.dumps(CompContents, indent=4))
    else:
        print("\nGlobal Query is Empty")
        log("Global Query is Empty")

#Main Execution
parser = argparse.ArgumentParser(prog='UCS Inventory Engine',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description="UCS Inventory script lets you query the component across multiple UCS domains",
                                 epilog=textwrap.dedent('''Thanks for using %(prog)s! \
                                         \nFor Further queries/suggestions Please reach out vivavila/rameseka'''))
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--add', 
                   nargs=3 ,
                   metavar=("IP","Username", "Password"),
                   help='Add a domain Info %(metavar)s to the Config File') 
group.add_argument('--get', action="store_true" ,help='Fetch the domains from the Config File')
group.add_argument('--remove', nargs=1, help='Remove the domain from the Config File')
group.add_argument('--rack',  nargs="?", const="all", help='Query the Rack server across domains')
group.add_argument('--blade', nargs="?", const="all", help='Query the Blade server across domains')
group.add_argument('--adapter', nargs="?", const="all", help='Query the Adapters across domains')
group.add_argument('--controller', nargs="?", const="all", help='Query the Storage Controller across domains')
group.add_argument('--disk', nargs="?", const="all", help='Query the Local Drives across domains')
args = parser.parse_args()
#Add a Custom usage
#If no queries specified print all
Welcome()

if args.add:
    if len(args.add) == 3:
        addDomain(args.add[0], args.add[1], args.add[2])
    else:
        parser.exit(1,message="\nPlease Provide Valid Number of Arguuments -a/--add <IP> <username> <Password>")

if args.get:
    getDomain(True)

if args.remove:
    if len(args.remove) == 1:
        removeDomain(args.remove[0])
    else:
        parser.exit(1,message="\nPlease Provide Valid Number of Arguuments -d/--remove <IP>")

if args.rack is not None:       
    if args.rack != "all":
        Component = "rack"
        SearchQuery = args.rack
        RetrieveQueryfromGlobalJsonResult()
    else:
        Component = "rack"
        print("\nNo Search Query passed, Printing all Rack Inventory Data across all the Domains\n")
        RetrieveQueryfromGlobalJsonResult()

if args.blade is not None:
    if args.blade != "all":
        Component = "blade"
        SearchQuery = args.blade
        RetrieveQueryfromGlobalJsonResult()
    else:
        Component = "blade"
        print("\nNo Search Query passed, Printing all Blade Inventory Data across all the Domains\n")
        RetrieveQueryfromGlobalJsonResult()

if args.adapter is not None:
    if args.adapter != "all":
        Component = "adapter"
        SearchQuery = args.adapter
        RetrieveQueryfromGlobalJsonResult()
    else:
        Component = "adapter"
        print("\nNo Search Query passed, Printing all Adapter Inventory Data across all the Domains\n")
        RetrieveQueryfromGlobalJsonResult()

if args.controller is not None: 
    if args.controller != "all":
        Component = "controller"
        SearchQuery = args.controller
        RetrieveQueryfromGlobalJsonResult()
    else:
        Component = "controller"
        print("\nNo Search Query passed, Printing all Storage Controller Inventory Data across all the Domains\n")
        RetrieveQueryfromGlobalJsonResult()
  
if args.disk is not None:  
    if args.disk != "all":
        Component = "disk"
        SearchQuery = args.disk
        RetrieveQueryfromGlobalJsonResult()
    else:
        Component = "disk"
        print("\nNo Search Query passed, Printing all Local Disk Inventory Data across all the Domains\n")
        RetrieveQueryfromGlobalJsonResult()

# """
# - Argparse Support  -- DONE
# - Multidomain Support -- DONE
# - Indexing Support   -- DONE
# - Integrate with Automation Engine
# - Add Logging Support
# """