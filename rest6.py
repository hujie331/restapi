
# import requests
# from pprint import pprint
#
# url = "http://172.19.195.39:3000/rpc/get-configuration"
#
# payload={}
# headers = {
#   'Authorization': 'Basic amh1MTpIVWppZUAyMDIyMDIyNw==',
#   'Accept': 'application/json',    # from junos rest-api explorer (mandatory)
#   'Content-Type': 'application/xml'
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# response_dict = response.json()
#
# pprint(response_dict)



import requests
from pprint import pprint

url = "http://172.19.195.39:3000/rpc/get-interface-information"

payload = "<interface-name>ae0</interface-name>"
headers = {
  'Authorization': 'Basic amh1MTpIVWppZUAyMDIyMDIyNw==',
  'Accept': 'application/json',        # from junos rest-api explorer (mandatory)
  'Content-Type': 'application/xml'
}

response = requests.request("POST", url, headers=headers, data=payload)
#print(type(response))             #<class 'requests.models.Response'>
response_dict = response.json()
#print(type(response_dict))        #<class 'dict'>
print(response_dict)
#pprint(response.text)
#print(response.text)