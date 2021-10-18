import requests

# response = requests.get('https://api.github.com/user', auth=('YorkshireGold', 'pass'))
# print(response.status_code)
# print(response.headers)
# print("----------------")
# print(response.encoding)
# print("----------------")
# print(response.text)
# print("----------------")
# print(response.json())



# New_Response = requests.post('https://httpbin.org/post', data={'key': 'value'})
# print(New_Response.text)


# del_Response = requests.delete('https://httpbin.org/delete')
# print(del_Response.status_code)
# print(del_Response.text)


# head_Response = requests.head('https://httpbin.org/get')
# print(head_Response.status_code)
# print(head_Response.text)

# options_Response = requests.options('https://httpbin.org/get')
# print(options_Response.status_code)
# print(options_Response.text)

# # --------------- Passing params ---------------
# payload = {'key1': 'value1', 'key2': 'value2'}
# payload_Response = requests.get('https://httpbin.org/get', params=payload)
# print(payload_Response.url)
# print(payload_Response)

# # --------------- Passing List of params ---------------
# payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
# List_of_params_Request = requests.get('https://httpbin.org/get', params=payload)
# print(List_of_params_Request.url)
# print(List_of_params_Request.text)

# # --------------- Response Content ---------------
# Response_Content_Request = requests.get('https://api.github.com/events')
# print(Response_Content_Request.text)

# # --------------- Response Content with Encodeing ---------------
# Response_Content_Request = requests.get('https://api.github.com/events')
# print(Response_Content_Request.text)
# Response_Content_Request.encoding = 'ISO-8859-1'
# print(Response_Content_Request.text)

# # --------------- Response Content with Encodeing ---------------
# Response_Content_Request = requests.get('https://api.github.com/events')
# print(Response_Content_Request.text)

# # --------------- JSON response data  ---------------
# Response_Content_for_JSON = requests.get('https://api.github.com/events')
# print(Response_Content_for_JSON.json())

# # --------------- JSON response data  ---------------
# Response_Content_for_JSON = requests.get('https://api.github.com/events')
# print(Response_Content_for_JSON.raise_for_status())

# --------------- Raw Response Content ---------------
Response_Content_for_JSON = requests.get('https://api.github.com/events', stream=True)
print(str(Response_Content_for_JSON.raw))
print("-----------------------")
print(str(Response_Content_for_JSON.raw.read(10)))  # will dusplay he first 10 bytes ( I thibk)

with open(filename, 'wb') as fd:
    for chunk in Response_Content_for_JSON.iter_content(chunk_size=128):
        fd.write(chunk)
