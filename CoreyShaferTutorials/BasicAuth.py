import requests
import time

# https://httpbin.org/ -- A simple HTTP Request & Response Service.
# 
# ---- Basic Auth


# auth are the credentials to pass to the request 
# /basic-auth/<USER>/<PW>
httpbin_Basic_Auth_Request = requests.get('https://httpbin.org/basic-auth/admin/supersecret',auth=('admin','supersecret')) 

if httpbin_Basic_Auth_Request.text :
    print(httpbin_Basic_Auth_Request.text)
else:
    print("No response received")

# Continue from 22.31  - https://www.youtube.com/watch?v=tb8gHvYlCFs&list=PLkno0u-EA5dzoKN2KIYf9N1iNa1FqrafV&index=9&t=382s