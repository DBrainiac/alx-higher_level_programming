#!/usr/bin/python3
import urllib.request
import sys

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode()

with urllib.request.urlopen(url, data) as response:
    response_body = response.read().decode('utf-8')
    print(response_body)

