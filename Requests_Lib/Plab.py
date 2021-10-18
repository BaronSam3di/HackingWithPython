import requests

# api-endpoint
URL = "http://ptl-d1bca9a6-2ae8e122.libcurl.so/pentesterlab"

Cookie = {'key':'please'}

# sending get request and saving the response as response object
response = requests.get(URL, Cookie)

print(response.text)

