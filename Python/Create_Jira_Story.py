import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask

app = Flask(__name__)

@app.route('/createjira', methods=['POST'])
def createjira():

    url = "https://your-url.atlassian.net/rest/api/3/issue"

    auth = HTTPBasicAuth("mail@gmail.com", "api-token")

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {
        "description": {
        "content": [
            {
            "content": [
                {
                "text": "Order entry fails when selecting supplier.",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },
        "issuetype": {
        "id": "10006"
        },
        "project": {
        "key": "DP"
        },    
        "summary": "Main order flow broken",
    },
    "update": {}
    } )

    
    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )
    webhook = request.json
    response = None
        if webhook['comment'].get('body') == "/jira":
            response = requests.request("POST", url, data=payload, headers=headers, auth=auth)
            return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
        else:
            print('Jira issue will be created if comment include /jira')
            
    # print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

if __name__ == '__main__':
  app.run("0.0.0.0", port=5000)
