#!/usr/bin/python3

import requests

from requests.auth import HTTPBasicAuth
# this is for supplying http basic authentication

cred=HTTPBasicAuth('root','cisco')
head={'Accept':'application/json'}

# head={'Accept':'text/html'} ---- This is default format
url="http://192.168.54.128/level/15/exec/-/sh/ip/int/br" 
# defining that data from that API in JSON format
# Now connection to restconf OR http protocol
output=requests.get(url,headers=head,auth=cred)
print(output)
#only giving HTTP response code
print(output.text)
# giving HTML based response






 
