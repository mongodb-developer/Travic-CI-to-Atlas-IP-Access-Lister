# Travic-CI-IP-Address-Whitelister

A script that pulls the list of IP Addresses that Travis CI uses
and whitelists them in MongoDB Atlas so that Travis CI can 
interact with databases on Atlas.

## Running the Script

Create a file named `dev.config`.  The file needs three constants:
- PUBLIC_KEY: Your Atlas Public API Key
- PRIVATE_KEY: Your Atlas Private API Key
- PROJECT_ID: The ID of the Atlas Project Where You Want to Add the Whitelist Entries

If you rename your config file, update the first line of whitelister.sh appropriately.

Run the script by executing `./whitelister.sh`.

## Related Resources
- [Travis CI's Documentation on IP Addresses](https://docs.travis-ci.com/user/ip-addresses/)
- [MongoDB's Documentation on Configuring Atlas API Access](https://docs.atlas.mongodb.com/configure-api-access/#programmatic-api-keys)
- [MongoDB's Documentation on Adding Entries to Project IP Whitelist](https://docs.atlas.mongodb.com/reference/api/whitelist-add-one/)
