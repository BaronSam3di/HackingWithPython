import requests
import time

# https://httpbin.org/ -- A simple HTTP Request & Response Service.

url = 'https://xkcd.com/365/'

pictureRequest = requests.get('https://imgs.xkcd.com/comics/python.png')

ThisRequest = requests.get(url)

print("The response code is ",ThisRequest)
print()
print("The attributes and methods are ",dir(ThisRequest))
print()
print("The Status code is ", ThisRequest.status_code)
print()
print("Is everyting ok ? (ie; < 400): ",ThisRequest.ok)     # ok is errors less than 400 . 500 is server errors.

# print("The help menu will follow in 3 seconds")
# time.sleep(3)   # sleeping for 3 mins
# print("The help menu is ",help(ThisRequest))          # needs to be removed somehow with press of q
# print()

with open('comic.png', 'wb') as newfile:                # wb == write bytes mode 
    newfile.write(pictureRequest.content)

print()
print("The headers are:")
print()
dictionary_items = ThisRequest.headers.items()
for item in dictionary_items:
    print(item[0] + " : "+ item[1])


# httpbin testing

payload = {'page':2, 'count':25}
httpbinRequest = requests.get('https://httpbin.org/get', params=payload)    # get needs params. Represented as args
print()
print("httpbin GET Request:", httpbinRequest.text)
print()
print("httpbin GET Request url:", httpbinRequest.url)
print()


payload = {'username':"Bob", 'Password':"testing"}
httpbinRequest = requests.post('https://httpbin.org/post', data=payload) # post needs data. Represented as Form
print()
print("httpbin POST Request:", httpbinRequest.text)
print()
print("httpbin POST Request url:", httpbinRequest.url)
print()


payload = {'Country':"France", 'City':"Paris"}
httpbinRequest = requests.post('https://httpbin.org/post', data=payload) # post needs data. Represented as Form
print()
print("httpbin POST Request as JSON:", httpbinRequest.json())           # json is a method , which wil make a dict from the json response
print()

response_dict = httpbinRequest.json()
print(response_dict['form'])