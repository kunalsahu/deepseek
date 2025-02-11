## Accessing deepseek model using python code.

import requests
import json

url = "http://localhost:11434/api/generate"

data = {
    "model": "deepseek-r1:1.5b",
    "prompt": "write python code for adding two number",
    "stream": False
}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
response = requests.post(url, data=json.dumps(data), headers=headers)
print(response.text)
print("Status Code:", response.status_code)
print("Response:", json.loads(response.text)['response'])


