from enum import Enum,unique,auto

@unique  # --> to prevent duplicate values assigned to Enum
class SoftwareEngineering(Enum):
    SDE_III=1
    SR_SDE=2
    SRE=3
    COMPUTER_SCIENTIST=4
    MTS=5
    MTS_III=auto()  #Automatically Assigns the values Sequentially
    SOFTWARE_DEVELOPER=5


#Print the Enum Name and Values
print(SoftwareEngineering.SRE.name,"-",SoftwareEngineering.SRE.value)

#Iterate over enums and print its name and values
for Role in SoftwareEngineering:
    print(Role.name,"-",Role.value)