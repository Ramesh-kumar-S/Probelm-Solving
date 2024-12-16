import time
from datetime import datetime, timedelta

def shedule_function(name, *args):
    pass

Now=datetime.now()
print(Now, type(Now))
FwdDate = Now + timedelta(seconds=500)
print(FwdDate, type(FwdDate), (FwdDate-Now))
total = Now + (FwdDate - Now)
print(datetime.now())
# print(time.time())
print(datetime.fromtimestamp(time.time()+100).strftime('%c'))
print(datetime.fromtimestamp(time.time()+100).strftime('%c'))