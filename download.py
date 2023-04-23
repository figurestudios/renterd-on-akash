import requests

url = 'http://URI:port/api/worker/objects/foo.txt'

auth = ('', 'yourpassword')

response = requests.get(url, auth=auth)

with open('foo.txt', 'wb') as f:
    f.write(response.content)
