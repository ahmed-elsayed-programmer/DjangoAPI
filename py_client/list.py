import requests 
from getpass import getpass , getuser

auth_endpoint = 'http://127.0.0.1:8000/api/auth/'
# user = getuser()
# password = getpass() 
auth_response = requests.post(auth_endpoint , json={"username" : 'ahmed' , 'password' : '123123'})
print(auth_response.text)


endpoint = 'http://127.0.0.1:8000/api/products'
if auth_response.status_code == 200 :
  token = auth_response.json()['token']
  headers = {
    'Authorization' : f'token {token}'
  }
  get_res = requests.get(endpoint , headers=headers )
  print(get_res.text)