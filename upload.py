import requests

url = 'http://URI:port/api/worker/objects/foo.txt'
data = open('foo.txt', 'rb').read()

headers = {
    'Content-Type': 'application/octet-stream'
}

auth = ('', 'yourpassword')

response = requests.put(url, data=data, headers=headers, auth=auth)

print(response.text)
