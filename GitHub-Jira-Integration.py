from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)

@app.route('/',methods=['POST'])
def create_jira():
    url = "https://your-domain.atlassian.net/rest/api/2/issue"
    auth = HTTPBasicAuth("abc@example.com", <API-token>)
    headers = {
      "Accept": "application/json",
      "Content-Type": "application/json"
      }
    payload = json.dumps( {
      "fields": {
        "description": "text issue",
        "issuetype": {
          "id": "10012"
          },
        "project": {
          "key": <Project-Name>
          },
        "reporter": {
          "id": <id>
          },
        "summary": "issue created by a user on GitHub",
        }
      } )
    response = requests.request(
      "POST",
      url,
      data=payload,
      headers=headers,
      auth=auth
      )
    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__=='__main__':
    app.run('0.0.0.0',debug=True)
