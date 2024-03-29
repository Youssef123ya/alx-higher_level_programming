#!/usr/bin/env python3
import urllib.request

# Open the URL using a with statement
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    # Read the response content
    content = response.read()

# Display the response body
print("Body response:")
print("\t- type: {}".format(type(content)))
print("\t- content: {}".format(content))
print("\t- utf8 content: {}".format(content.decode('utf-8')))

