import requests
from requests.auth import HTTPDigestAuth
from pprint import pprint
import configparser

# Get the config file
Config = configparser.ConfigParser()
Config.read("dev.ini")

# Get information about the projects
groups = requests.get('https://cloud.mongodb.com/api/atlas/v1.0/groups', auth=HTTPDigestAuth(Config.get('Atlas', 'PUBLIC_KEY'), Config.get('Atlas', 'PRIVATE_KEY')))
print(groups)
pprint(groups.json())
