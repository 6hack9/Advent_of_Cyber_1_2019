import requests

path = ''
host = 'http://10.10.169.100:3000/'

value = ''

while(path != 'end'):
	response = requests.get(host + path)
	print(response)
	#status_code = response.status_code
	#print(status_code)

	json_response = response.json()

	value += json_response['value']
	path = json_response['next']
	print(path + " ")
	print(value)

print(value)