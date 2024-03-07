Name="Software Engineer"

# def cleanUp():
try:
    print(Name[26])
    Res=Name[26]
except IndexError:
    print("Specified Index Doesn't Exist")
finally:
    print("Cleanup Action")
    
# cleanUp()
