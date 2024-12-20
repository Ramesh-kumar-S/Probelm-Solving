#!/usr/bin/python3
#########################################################################################################
#      Avenger.sh  : Ease the way of generating the Certificates for KMIP Configurations                 #
#       Author     : Ramesh Kumar Sekar                                                                  #
#          Usage   : script.py --config/unconfig                                                           #                                                     #
##########################################################################################################
import json
import os
import argparse
import textwrap
import sys
import stat
from collections import defaultdict
from functools import wraps
import logging
import ssl
import requests
from requests.exceptions import HTTPError

"""
- Get the Name and CSR
- Create Client Profile , If not exists
- Create Registration token 
- Register the Client 
- Save the CSR and Download it
"""


class Logging_Handler:
    """ Class handles Log handlers 

    Methods:
        log 
            Receives the log-level ,message and logs it respectively.
        _function_logger
            Logs the function entry and exit calls
    """

    def __init__(self):
        """ Initializes the Logging"""
        self.log_file_path = 'SED_Handler.log'

        with open(self.log_file_path, 'w'):
            pass
        os.chmod(self.log_file_path, stat.S_IRWXU |
                 stat.S_IRWXG | stat.S_IRWXO)

        logging.basicConfig(
            filename=self.log_file_path,
            level=logging.DEBUG,
            datefmt="%Y:%m:%d %I:%M:%S %p",
            format="%(asctime)s: %(levelname)s %(funcName)s:%(lineno)d %(module)s - %(message)s",
            filemode='w'
        )
        self.logger = logging.getLogger(__name__)

    def log(self, level, message):
        """ 
            Logs the message according to the log level 
        """
        if isinstance(message, dict):
            message = json.dumps(message, indent=4)

        if level == "INFO":
            self.logger.info(message)
        elif level == "DEBUG":
            self.logger.debug(message)
        elif level == "CRITICAL":
            self.logger.critical(message)
        elif level == "ERROR":
            self.logger.error(message)
        else:
            self.logger.warning(message)

    @staticmethod
    def _function_logging(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger = logging.getLogger(__name__)
            logger.info(f"Executing function: {func.__name__}")  # Print args
            result = func(*args, **kwargs)
            logger.info(f"Exitting function: {func.__name__}")
            return result
        return wrapper


class RESPONSE:
    """ 
        Class to validate the HTTP Status codes 
    """
    AUTH_SUCCESS = 200
    PROFILE_CREATION_SUCCESS = 201
    PROFILE_DELETION_SUCCESS = 204
    LOGIN_FAILED = 401
    VALIDATION_ERROR = 422


class Authentication(Logging_Handler):
    """ 
        Class that's used for authentication, sending and receiving configurations.

    Attributes:
            - None
    Methods :
         _sendConfig(self, URI, data=None, headers=None, method="POST") 
                 Pushes the config to the Thales Portal.
         _getJWTtoken(self)
                 Fetches the JWT Token for the token response.
         _refreshToken(self)
                 Re-Authenticates the existing JWT token.
    """

    def __init__(self, userId, password):
        """
            Instantiates the Authentication class

        Parameters:
            userId (str): The user ID for authentication.
            password (str): The password for authentication.
        Attributes:
              ssl_context (SSLContext): Manages SSL settings and certificates.
              userId (str): Credentials used to authenticate with Thales.
              password (str): Credentials used to authenticate with Thales.
              status_code (int): Stores the response HTTP status code.
        """
        requests.packages.urllib3.disable_warnings(
            requests.packages.urllib3.exceptions.InsecureRequestWarning)
        super().__init__()  # Call LoggingHandler's __init__
        self.ssl_context = ssl.create_default_context()
        self.ssl_context.check_hostname = False
        self.ssl_context.verify_mode = ssl.CERT_NONE
        self.userId = userId
        self.password = password

    @Logging_Handler._function_logging
    def _sendConfig(self, URI, data=None, headers=None, method="POST"):
        """
            Sends an configuration to the Thales via REST API

        Parameters
        URI(str) : REST API URI
        data(dict, optional) : The configuration payload. Defaults to None.
        headers(dict, optional) : The API headers. Defaults to None
        method(str, optional) : The HTTP method to use (GET/POST). Defaults to "POST".
        """
        URL = "https://" + URI
        if headers is None:
            headers = {'Content-Type': 'application/json',
                       'Accept': 'application/json'
                       }
        # What if the Data is None
        json_data = json.dumps(data) if data is not None else None
        response_json = None

        self.log("INFO", headers)
        self.log("INFO", json_data)
        try:
            if method == "POST":
                response = requests.post(
                    URL, headers=headers, data=json_data, verify=False)
            elif method == "DELETE":
                self.log("INFO", "sending DELETE Request")
                response = requests.delete(URL, headers=headers, verify=False)
            else:
                self.log("INFO", "sending GET Request")
                response = requests.get(URL, headers=headers, verify=False)

            self.status_code = response.status_code
            # Delete Request won't provide any response
            if method != "DELETE":
                response_json = response.json()
                self.log("DEBUG", response_json)

            self.log("INFO", f'HTTP Status Code : {self.status_code}')
        except HTTPError as e:
            print('Error:', e.reason)
            self.log("ERROR", e.reason)
            response_json = None
        except Exception as e:
            print('Error:', str(e))
            self.log("ERROR", str(e))
            response_json = None
        return response_json

    @Logging_Handler._function_logging
    def _getJWTtoken(self):
        """
            Parses the JWT token from the authentication token response
        """
        Auth_URI = ""
        Payload = {
            "grant_type": "password",
            "username": self.userId,
            "password": self.password,
            "domain": "",
            "auth_domain": "",
            "refresh_token_revoke_unused_in": 60
        }
        headers = {'Content-Type': 'application/json',
                   'Accept': 'application/json'
                   }
        response = self._sendConfig(Auth_URI, Payload, headers, method="POST")
        Jwt_token = response.get("jwt") if response else None
        self.log("INFO", f'Fetched the JWT Token : {Jwt_token}')
        return Jwt_token

    @Logging_Handler._function_logging
    def _refreshToken(self):
        """Re-Authenticates the JWT Token"""
        pass


class ClientProfile(Authentication):
    """ Class used for profile CRUD Operaions.

    Methods :
        listProfiles(self)
                 Fetches the available client profiles.
        isProfileAlreadyPresent(self, Name):
                 Validate if the user-specified profile is already present.
        fetch_csr(self)
                 Parses the user specified multi-line CSR
        createProfile(self, Name):
                 Creates an Client Profile.
        fetch_registration_token(self):
                 Generates an registration token with created client profile.
        client_registration(self)
                 Registers the generated token and print the certificates
    """

    def __init__(self, userId, password):
        """
            Instantiates the ClientProfile class and Inherits the methods from Authentication class

        Parameters:
            userID(str) : Credentials used to authenticate with Thales
            password(str) : Credentials used to authenticate with Thales

        Attributes:
            AuthObj(object) - Authentication class object
            JwtToken(str) - JWToken fetched from the token response
        """
        super().__init__(userId, password)
        self.AuthObj = Authentication(self.userId, self.password)
        self.JwtToken = self.AuthObj._getJWTtoken()  # If JWT token is NONE, Handle it

    def listProfiles(self):
        """
            Fetches the available profiles
        """
        headers = {'Accept': 'application/json',
                   'authorization': "Bearer " + self.JwtToken
                   }
        List_Profiles_URI = ""
        Payload = {"Skip": 0}
        response = super()._sendConfig(List_Profiles_URI, Payload, headers, method="GET")
        json_response = json.dumps(response, indent=4)

    @Logging_Handler._function_logging
    def isProfileAlreadyPresent(self, Name):
        """ 
            Validates the profile is already present 
        """
        headers = {'Accept': 'application/json',
                   'authorization': "Bearer " + self.JwtToken
                   }
        Fetch_Profile_URI = f"/{Name}"
        response = super()._sendConfig(Fetch_Profile_URI, headers=headers, method="GET")
        if self.status_code == RESPONSE.AUTH_SUCCESS:
            print(f'\nProfile with "{Name}" already exists.')
            self.log("INFO", f'\nProfile with "{Name}" already exists.')
            return True
        return False

    @Logging_Handler._function_logging
    def fetch_csr(self):
        """ 
            Parses the user-specified multi-line CSR 
        """
        print("\nPaste the CSR & Enter twice...\n")
        Res = ""
        while True:
            line = input()
            if line == "":
                break
            Res += f'\n{line}'
        return Res

    @Logging_Handler._function_logging
    def client_registration(self):
        """ 
            Registers the generated profile token and prints the client 
        """
        Cliet_Registration_URI = ""
        headers = {'Content-Type': 'application/json',
                   'Accept': 'application/json',
                   'authorization': "Bearer " + self.JwtToken
                   }
        Payload = {
            "name": f'{self.profile_name}_RegClient',
            "reg_token": self.reg_token,
            "ext_cert": ""
        }

        response = self._sendConfig(
            Cliet_Registration_URI, Payload, headers=headers)
        if self.status_code == RESPONSE.PROFILE_CREATION_SUCCESS:
            Cert = response["cert"]
            self.log("INFO", Cert)
            os.system('clear')
            print(Cert)

    @Logging_Handler._function_logging
    def fetch_registration_token(self, isClientRegistration=True):
        """ 
            Creates an registration token and fetches the token 
        """
        self.registration_token_name = f'{self.profile_name}_RegToken'
        Token_Registration_URI = ""
        headers = {'Content-Type': 'application/json',
                   'Accept': 'application/json',
                   'authorization': "Bearer " + self.JwtToken
                   }
        Payload = {
            "name_prefix": self.registration_token_name,
            "lifetime": "",
            "cert_duration": 730,
            "ca_id": "7a4c99ea-e15a-4ca9-8cc0-c8a9ae388ba5",
            "max_clients": 100,
            "client_management_profile_id": "",
            "profile_name": self.profile_name
        }
        response = self._sendConfig(
            Token_Registration_URI, Payload, headers=headers)
        if self.status_code == RESPONSE.PROFILE_CREATION_SUCCESS:
            self.reg_token = response["token"]
            self.log("INFO", f'Generated the Registration token for the Profile {
                     self.reg_token} - {self.profile_name}\n\n')
            print(f'\nGenerated the Registration token [{
                  self.reg_token}] for the Profile {self.profile_name}\n\n')
        if isClientRegistration:
            self.client_registration()
        else:
            self.log("INFO", f'Skipping Client Registration and CSR Generation')
            return response

    @Logging_Handler._function_logging
    def createProfile(self, Name):
        """ 
            Creates an client profile
        """
        self.Name = Name
        if self.isProfileAlreadyPresent(self.Name):
            print(
                f"\nClient profile already exists with the specified Name -> {self.Name}")
            return
        self.CSR_Cert = self.fetch_csr()

        Create_Profile_URI = ""
        headers = {'Content-Type': 'application/json',
                   'Accept': 'application/json',
                   'authorization': "Bearer " + self.JwtToken
                   }
        Payload = {
            "name": self.Name,
            "do_not_modify_subject_dn": True,
            "properties": {
                "csr": self.CSR_Cert,
                "cert_user_field": "OU"
            },
            "device_credential": {
                "serial_no": "",
                "device_id": "",
                "network_id": "",
                "machine_id": "",
                "media_id": "",
                "password": ""
            }
        }

        response = self._sendConfig(
            Create_Profile_URI, Payload, headers=headers)
        if self.status_code == RESPONSE.PROFILE_CREATION_SUCCESS:
            self.profile_name = response["name"]
            self.profile_id = response["id"]
            print(f"\nClient profile {self.Name} has been created")
            print(
                f"\nProfile Info - Name : {self.profile_name} with ID : {self.profile_id}")

            self.log("INFO", f"Client profile {self.Name} has been created")
            self.log(
                "INFO", f"Profile Info - {self.profile_name} - {self.profile_id}")

            # Fetching the Registration Token for the created profile
            self.fetch_registration_token()

    @Logging_Handler._function_logging
    def delete_client(self, Name):
        """
            Delete the Registration Client
        """
        self.Name = Name
        headers = {'Content-Type': 'application/json',
                   'Accept': 'application/json',
                   'authorization': "Bearer " + self.JwtToken
                   }

        List_Client_URI = f""
        Payload = {
            "name": f'{self.Name}_RegClient'
        }
        response = self._sendConfig(
            List_Client_URI, Payload, headers=headers, method="GET")
        if self.status_code == RESPONSE.AUTH_SUCCESS:
            if response["resources"][0]["profile_name"] == Name and response["resources"][0]["name"] == f'{Name}_RegClient':
                client_id = response["resources"][0]["id"]

                Delete_client_URI = f"/{client_id}"
                response = self._sendConfig(
                    Delete_client_URI, headers=headers, method="DELETE")
                if self.status_code == RESPONSE.PROFILE_DELETION_SUCCESS:
                    self.log(
                        "INFO", f'{self.Name}_RegClient has been deleted successfully.')
                    print(
                        f'\n{self.Name}_RegClient has been deleted successfully.')
                    self.log(
                        "INFO", f'Proceeding to delete the Registration token')
                    self.delete_profile(self.Name)
                    # self.delete_registration_token(self.Name)

    def delete_registration_token(self, Name):
        """ 
            Deletes the generated the Registration token
        """
        self.profile_name = Name

        response = self.fetch_registration_token(isClientRegistration=False)
        registrationToken_id = response["id"]
        token = response["token"]
        token_name = response["name_prefix"]
        profile_name = response["label"]["KmipClientProfile"]

        if profile_name == self.Name and token_name == f'{token_name}_RegToken':
            Delete_RegistrationToken_URI = f"{registrationToken_id}"
            headers = {'Content-Type': 'application/json',
                       'Accept': 'application/json',
                       'authorization': "Bearer " + self.JwtToken
                       }
            response = self._sendConfig(
                Delete_RegistrationToken_URI, headers=headers, method="DELETE")

            if self.status_code == RESPONSE.PROFILE_DELETION_SUCCESS:
                self.log("INFO", f'Registration token : {
                         token_name} has been deleted successfully.')
                print(f'Registration token : {
                      token_name} has been deleted successfully.')
                self.log(
                    "INFO", f'Proceeding to delete the Client Profile - {self.Name}')
                self.delete_profile(self.Name)

    @Logging_Handler._function_logging
    def delete_profile(self, Name):
        """
            Delete the client profile
        """
        if self.isProfileAlreadyPresent(self.Name):
            self.log(
                "INFO", f"\nClient profile already exists with the specified Name -> {self.Name}")
            self.log("INFO", f"\Proceeding to delete {self.Name}")

            Delete_Profile_URI = f"/{self.Name}"
            headers = {'Content-Type': 'application/json',
                       'Accept': 'application/json',
                       'authorization': "Bearer " + self.JwtToken
                       }
            response = self._sendConfig(
                Delete_Profile_URI, headers=headers, method="DELETE")

            if self.status_code == RESPONSE.PROFILE_DELETION_SUCCESS:
                self.log("INFO", f'{self.Name} has been deleted successfully.')
                print(f'\n{self.Name} has been deleted successfully.')
                return

        else:
            print(
                f"\nNo Client profile exists with the specified Name -> {self.Name}")
            self.log(
                "INFO", f"\nNo Client profile exists with the specified Name -> {self.Name}")
            return


requests.packages.urllib3.disable_warnings(
    requests.packages.urllib3.exceptions.InsecureRequestWarning)


def Welcome():
    """ 
        Starts the Logging 
    """
    Ret_Val = os.system('clear')
    print(140*"-")
    print("SED Management Handler V1.1".center(140))
    print(140*"-")

# Main Program Execution starts here


def main():
    """
        Main Program Execution 
    """
    os.system('clear')
    print(140*"-")
    print("KMIP Handler V1.1".center(140))
    print(140*"-")

    parser = argparse.ArgumentParser(prog='KMIP Handler v1.1',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description="KMIP Handler to generate the Certificates",
                                     epilog=textwrap.dedent('''Thanks for using %(prog)s! \
                                \nFor Further queries/suggestions Please reach out rameseka'''))

    parser.add_argument('--config', action='store_true',
                        help='Generate the CSR')
    parser.add_argument('--unconfig', action='store_true',
                        help='Deletes the Profile, Token, Client  from  the KMIP Portal')
    args = parser.parse_args()

    if args.config:
        C = ClientProfile("", "")
        ProfileName = input("\nPlease enter the profile name : ")
        C.createProfile(ProfileName)
    elif args.unconfig:
        C = ClientProfile("", "")
        ProfileName = input("\nPlease enter the profile name : ")
        C.delete_client(ProfileName)
    else:
        parser.exit(
            1, message="\nPlease Provide Valid arguments <Script.py> --config/--unconfig\n\n")


if __name__ == "__main__":
    main()
