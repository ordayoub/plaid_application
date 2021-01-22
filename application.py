import requests
import json

url = "https://contact.plaid.com/jobs"

data = {
    "name": "Owen Dayoub",
    "email": "xxxxxxx",
    "resume": "xxxxxxxxxx",
    "phone": "xxxxxxxxxxxxxx",
    "job_id": "488bcd3f-2227-4b72-8b69-bf3bc519bde5",
    "github": "https://github.com/ordayoub",
    "location": "xxxxxxxxxxx",
    "favorite_candy": "Sour Gummy Worms",
    "superpower": "reaching the top shelf"
}
data = json.dumps(data)

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

http_post_request = requests.post(url=url, data=data, headers=headers)

server_response = http_post_request.text

print(server_response)
