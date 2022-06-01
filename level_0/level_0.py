#!/usr/bin/python3
import requests

host = "http://158.69.76.135/level0.php"
payload = {'id': '4597', 'holdthedoor': 'submit'}
for i in range(1024):
    req = requests.post(host, payload)
