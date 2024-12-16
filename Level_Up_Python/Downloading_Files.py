import requests

def download_file(URL, DestnPath):
    response = requests.get(URL)
    
    if response.status_code == 200:
        with open("Test.jpg", mode="wb") as file:
            file.write(response.content)

# download_file('http://699340.youcanlearnit.net/image001.jpg', r'C:\Users\rameseka\OneDrive - Cisco\Desktop\Ramesh Scripts\Probelm-Solving\Level_Up_Python')
# download_file('http://699340.youcanlearnit.net/image001.jpg', r'C:\Users\rameseka\OneDrive - Cisco\Desktop\Ramesh Scripts\Probelm-Solving\Level_Up_Python')

import pandas as pd
a = [[1,2], [2,5]]
rp = pd.DataFrame(a)
res = rp.to_dict()
print(res)