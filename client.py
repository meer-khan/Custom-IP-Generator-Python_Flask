import requests

req = requests.post(url='http://127.0.0.1:5000/IPgetter',
                    data={"zipCode":50000}, 
                    )