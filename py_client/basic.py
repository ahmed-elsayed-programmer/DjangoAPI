import requests 

endpoint = "https://httpbin.org/anything" 
endpoint = 'http://127.0.0.1:8000/api/'

get_res = requests.get(endpoint , json={'product_id' : 123})
print(get_res.headers)
print("_______________________________________")
print(get_res.text)