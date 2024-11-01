import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://your-domain.atlassian.net/rest/api/2/issue"
auth = HTTPBasicAuth("abc@example.com", <API-Token>)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

# We are defining only mandatory values down here.
payload = json.dumps( {
  "fields": {
    "description": "first story issue",
    "issuetype": {
      "id": "10014"
    },
    "project": {
      "key": <project-key>
    },
    "reporter": {
      "id": <account-id>
    },
    "summary": "story for first task made using python",
  }
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
