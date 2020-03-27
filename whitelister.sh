. dev.config

# Get the list of IP addresses that Travis CI uses
addresses=$(dig +short nat.travisci.net | sort)

# Create the array of objects for the IP addresses we want to whitelist
data='['

for address in $addresses
do
   data+='{"ipAddress" : "'
   data+=$address
   data+='", "comment" : "IP address for Travis CI" },' 
done

# Remove the trailing comma at the end of data
data=${data%?}

# Close the array
data+=']'

# Whitelist the IP addresses in Atlas
curl --user "$PUBLIC_KEY:$PRIVATE_KEY" --digest --include \
   --header "Accept: application/json" \
   --header "Content-Type: application/json" \
   --request POST "https://cloud.mongodb.com/api/atlas/v1.0/groups/$PROJECT_ID/whitelist?pretty=true" \
   --data "$data"
