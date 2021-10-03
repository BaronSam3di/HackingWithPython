# importing the requests library
import requests

# api-endpoint
URL = "https://webhook.site/43f90585-89df-4623-b60c-2494a78e4504"
URL2 = "https://www.geeksforgeeks.org/get-post-requests-using-python/"

# sending get request and saving the response as response object
response = requests.get(url = URL2)

# print(dir(response))  # shows all the attributes available of the response

# print(help(response))  # good way to see what our options are 

print(response.text)

