import json
import pandas as pd
import datetime
import requests
from requests.auth import HTTPBasicAuth
    
jenkins_url = "https://jenkinsurl/job/JOB_NAME/api/json?tree=builds[number,displayName,result,timestamp,duration]"  #Replace jenkinsurl(http,https),JOB_NAME with actual value
response_json = requests.get(jenkins_url, auth=HTTPBasicAuth('username', 'password')).json()
with open("report.json", "w") as file:
    json.dump(response_json, file)
with open("report.json", "r") as file:
    data = json.load(file)
    
builds_data = data['builds']

# Convert JSON to DataFrame
df = pd.json_normalize(builds_data)

# Rename columns
df.rename(columns={
    '_class': 'Class',
    'displayName': 'Display Name',
    'duration': 'Duration',
    'number': 'Number',
    'result': 'Result',
    'timestamp': 'Timestamp'
}, inplace=True)

# Convert timestamp and duration (if required)
df['Timestamp'] = df['Timestamp'].apply(lambda x: datetime.datetime.fromtimestamp(x / 1000).strftime('%Y-%m-%d %H:%M:%S'))
df['Duration'] = df['Duration'].apply(lambda x: f"{x // 3600000} hours, {(x % 3600000) // 60000} minutes, {(x % 60000) // 1000} seconds")

# Write DataFrame to Excel
df.to_excel('Report_Name.xlsx', index=False)
