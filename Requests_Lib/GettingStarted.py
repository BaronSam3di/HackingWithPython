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

# # --------------- Raw Response Content ---------------
# Response_Content_for_JSON = requests.get('https://api.github.com/events', stream=True)
# print(str(Response_Content_for_JSON.raw)) # .raw is the rawest form. 
# print("-----------------------")
# print(str(Response_Content_for_JSON.raw.read(10)))  # will display he first 10 bytes ( I think)


# # --------------- Raw Response Content ---------------
# Response_Content_for_a_File = requests.get('https://api.github.com/events', stream=True)
# with open("NewFile.txt", 'wb') as fd:               # wb == Write binary
#     for chunk in Response_Content_for_a_File.iter_content(chunk_size=128):
#         # .iter_content will handle a lot of what you would otherwise have to handle when using Response.raw directly.
#         fd.write(chunk)     # save what is being streamed to a file


# # --------------- Custom Headers ---------------
# some_custom_headers = {'user-agent': 'my-app/0.0.1'}
# custom_headers_response = requests.get('https://httpbin.org/get', headers=some_custom_headers)
# print(custom_headers_response.text)

# # ----------More complicated POST requests -------
# Some_payload = {'key1': 'value1', 'key2': 'value2'}
# response_complicated_post = requests.post("https://httpbin.org/post", data=Some_payload)
# print(response_complicated_post.text)


# # ------
# payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
# tuples_Response = requests.post('https://httpbin.org/post', data=payload_tuples)

# payload_dict = {'key1': ['value1', 'value2']}
# dict_Response = requests.post('https://httpbin.org/post', data=payload_dict)

# print(tuples_Response.text)
# print("--------------------")
# print(dict_Response.text)

# # --------------- json parameter ---------------
# payload = {'some': 'data'}
# json_Response = requests.post('https://httpbin.org/post', json=payload)
# print(json_Response.text)

# -------- POST a Multipart-Encoded File --------
# url = 'https://httpbin.org/post'
# files_to_send = {'file': open('NewFile.txt', 'rb')}
# file_send_response = requests.post(url, files=files_to_send)
# # print(file_send_response.text) # WARNING : massive payload in terminal
# ## To stream the request for multipart data check out : https://toolbelt.readthedocs.io/

# # # ------------ Response Status Codes ------------
# status_code_response = requests.get('https://httpbin.org/get')
# print(status_code_response.status_code)
# print(status_code_response.status_code == requests.codes.ok)


# ---------  raise for status only on "Bad request"  ---------
# bad_r = requests.get('https://httpbin.org/status/404')
# print(bad_r.status_code)
# print()
# bad_r.raise_for_status()

# # # ------------ headers Response ------------
# headers_response = requests.get('https://httpbin.org/get')
# print(headers_response.headers) 
# # Note: HTTP Header names are case-insensitive.
# print(headers_response.headers['Content-Type'])
# print(headers_response.headers['content-type'])


# # ------------------ Cookies ------------------
# cookies_data = dict(cookies_are='working')
# cookie_response = requests.get('https://httpbin.org/cookies', cookies=cookies_data)
# print(cookie_response.text)
# '''
# Cookies are returned in a RequestsCookieJar,
# which acts like a dict but also offers a more complete interface,
# suitable for use over multiple domains or paths. 
# Cookie jars can also be passed in to requests:
# '''
# jar = requests.cookies.RequestsCookieJar()
# jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')

# # If we set path to elsewhere they wont appear when visiting the url
# jar.set('gross_cookie', 'bleach', domain='httpbin.org', path='/elsewhere')
# url = 'https://httpbin.org/cookies'
# cookie_jar_response = requests.get(url, cookies=jar)
# print(cookie_jar_response.text)

# # ----------- Redirection and History -----------
# Redirection_Response = requests.get('http://google.com/')
# print(Redirection_Response.url)
# print(Redirection_Response.status_code)
# print(Redirection_Response.history)

# Timeouts
Redirection_Response = requests.get('http://google.com/', timeout=0.001) # 0.001 is too small to response and will invoke the error for demonstration