#!/usr/bin/python3
import requests

response = requests.get("https://alx-intranet.hbtn.io/status")

for key, value in response.json().items():
    print("\t-", key + ":", value)

