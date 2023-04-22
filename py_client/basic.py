import requests 

endpoint = "https://httpbin.org/anything" 

get_res = requests.get(endpoint)

print(get_res.text)