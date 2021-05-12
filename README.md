# CI/CD-Tool-Atlas-IP-Access-Lister

This repo contains a collection of scripts that pull IP addresses from various CI/CD tools and adds them to the MongoDB Atlas Access List.  The repo currently contains scripts for Travis CI and GitHub Actions.

## Travis CI

The following sections contain information about the script for adding Travis CI's IP addresses to the Atlas access list.

### Running the Script

Create a file named `dev.config`.  The file needs three constants:
- PUBLIC_KEY: Your Atlas Public API Key
- PRIVATE_KEY: Your Atlas Private API Key
- PROJECT_ID: The ID of the Atlas Project Where You Want to Add the IP Access List Entries

If you rename your config file, update the first line of accesslister.sh appropriately.

Run the script by executing `./accesslister.sh`.

### Related Resources
- [Travis CI's Documentation on IP Addresses](https://docs.travis-ci.com/user/ip-addresses/)
- [MongoDB's Documentation on Configuring Atlas API Access](https://docs.atlas.mongodb.com/configure-api-access/#programmatic-api-keys)
- [MongoDB's Documentation on Adding Entries to Project IP Access List](https://docs.atlas.mongodb.com/security/ip-access-list/)

## GitHub Actions

The following sections contain information about the script for adding GitHub Actions' IP addresses to the Atlas access list.

### Running the Script

To run this script, you will need [Python installed](https://www.python.org/downloads/). You will also need to install configparser using a command like the following:

```pip3 install configparser```

Create a file named `dev.ini`.  The file should be of the following format:

```
[Atlas]
PUBLIC_KEY: Your_Atlas_Public_API_Key
PRIVATE_KEY: Your_Atlas_Private_API_Key
PROJECT_ID: The_ID_of_the_Atlas_Project_Where_You_Want_to_Add_the_IP_Access_List_Entries
```

If you rename your config file, update line 8 of github-actions-access-lister.py appropriately.

Run the script by executing `python3 github-actions-access-lister.py`.

### Related Resources
- [GitHub Action's Documentation on IP Addresses](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners#ip-addresses)
- [MongoDB's Documentation on Configuring Atlas API Access](https://docs.atlas.mongodb.com/configure-api-access/#programmatic-api-keys)
- [MongoDB's Documentation on Adding Entries to Project IP Access List](https://docs.atlas.mongodb.com/security/ip-access-list/)
