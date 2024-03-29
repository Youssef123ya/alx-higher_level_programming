import requests
import sys

url = 'http://0.0.0.0:5000/search_user'
if len(sys.argv) < 2:
    q = ""
else:
    q = sys.argv[1]

data = {'q': q}
response = requests.post(url, data=data)

try:
    data = response.json()
    if data:
        print("[{}] {}".format(data.get('id'), data.get('name')))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
