import requests
from requests.auth import HTTPDigestAuth
from pprint import pprint
import configparser

# Get the config file
Config = configparser.ConfigParser()
Config.read("dev.ini")

# Get the list of IP Addresses that GitHub uses
ipAddresses = requests.get('https://api.github.com/meta').json()["actions"]

# Format the IP Addresses to have associated comments that we will store in Atlas
data = []
for address in ipAddresses:
    data.append({
        "ipAddress": address,
        "comment": "IP Address for GitHub Actions"
    })

# Make the POST request to add the IP addresses to the Access List
r = requests.post(url=f"https://cloud.mongodb.com/api/atlas/v1.0/groups/{Config.get('Atlas', 'PROJECT_ID')}/accessList?pretty=true",
                  auth=HTTPDigestAuth(Config.get('Atlas', 'PUBLIC_KEY'), Config.get('Atlas', 'PRIVATE_KEY')), json=data)

pprint(r.json())
pprint(r)
