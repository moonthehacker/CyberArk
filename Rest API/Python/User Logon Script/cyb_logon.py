import requests
import json
import csv

url = "https://win-06to9mso1c5/PasswordVault/API/Auth/CyberArk/Logon"

payload = "{\n\t\"username\": \"pimadmin\",\n\t\"password\": \"Cisco@123\",\n\t\"concurrentSession\": \"True\" }"
headers = {
		'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)


if response.status_code == 200:
	print('Login Sucessfull')
else:
	print('Login failed')



def list_safes(TOKEN):
	url = "https://win-06to9mso1c5/PasswordVault/api/Safes"
	payload={}
	headers = {
		'Content-Type': 'application/json',
		'Authorization' : TOKEN.strip('"')
	}
	response = requests.request("GET", url, headers=headers, data=payload, verify=False)
	print(response.text)
	print(TOKEN)




list_safes(response.text)

with open('accounts.csv','r') as f:
	csv_reader = csv.reader(f)
	print(csv_reader)

