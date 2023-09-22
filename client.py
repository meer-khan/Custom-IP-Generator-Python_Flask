import requests

custom_ip = '1.2.3.4'
req = requests.post(url='http://192.168.100.17:5001/IPgetter',
                    data={"zipCode":50000}, 
                    headers = {
                    'X-Forwarded-For': custom_ip, }
                    )


print (req.status_code)