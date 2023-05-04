#!/usr/bin/env python

import requests

url = "https://api.acoustid.org/v2/lookup"
# url = "https://api.acoustid.org/v2/submit"
data = {
    "client": "kkAUAzcqZu",
    "duration": "15",
    "fingerprint": "", 
}

response = requests.post(url, params=data)

print("Status Code", response.status_code)
print("JSON Response ", response.json())
