import requests

custom_ip = '1.2.3.4'
req = requests.post(url='http://127.0.0.1:5000/IPgetter',
                    data={"zipCode":50000}, 
                    headers = {
                    'X-Forwarded-For': custom_ip, }
                    )


print (req.data)