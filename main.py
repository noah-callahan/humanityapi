import requests
import json


auth_url = "https://www.humanity.com/oauth2/token.php"
auth_dict = {
    "client_id": "null",
    "client_secret": "null",
    "grant_type": "password",
    "username": "null",
    "password": "null",
    "redirect_uri": ""
}

employees_arr= []


print(auth_dict)

r = requests.post(auth_url,auth_dict)
print(r)
print(r.text)
parsed_access_token = json.loads(r.text)

request_url_dict = {"get_url":f"https://www.humanity.com/api/v2/me?access_token={parsed_access_token['access_token']}","employees_url":f"https://www.humanity.com/api/v2/employees?access_token={parsed_access_token['access_token']}"}



authed_req = requests.get(request_url_dict['get_url'])
employees_response = requests.get(request_url_dict['employees_url'])

parsed_authed_get = json.loads(authed_req.text)
parsed_employees = json.loads(employees_response.text)

print(parsed_employees['data'])

def grab_employees(employees):
    for i in employees:
        employees_arr.append({"id":i['id'],"name":i['name'],"username":i['username']})
  


grab_employees(parsed_employees['data'])

print(employees_arr)




