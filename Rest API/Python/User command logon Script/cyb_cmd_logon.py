import requests
import csv
import json
import stdiomask

TOKEN =''

def User_Login():

	build_url = input("Enter PVWA URL (format: https://win-06to9mso1c5): ")
	user = input("Onboarding User: ")
	pswd = stdiomask.getpass()

	url =  build_url+"/PasswordVault/API/Auth/CyberArk/Logon"
	build_payload = {"username": user,"password": pswd,"concurrentSession":"True"}
	payload = json.dumps(build_payload, indent=4)
	
	headers = {
		'Content-Type': 'application/json'
        }
	response = requests.request("POST", url, headers=headers, data= payload, verify= False)

	if response.status_code == 200:
		print('Login Sucessfull')
	else:
		print('Login failed')
	TOKEN = response.text

	


	
User_Login()
