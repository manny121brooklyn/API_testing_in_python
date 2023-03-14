import requests
header = {
    'Accept':'text/plain'
}
response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Activities/5', headers = header)
print(response.status_code) #print status code
print(response.json()) #print json message body

assert response.status_code == 200 #assert status code == 200
'''
headers= is used to pass header info, eg. as above
'''