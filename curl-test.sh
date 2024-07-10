#!/bin/bash

# Create a random POST request and getting the id field for deletion.
post_id=$(curl -X POST http://localhost:5000/api/timeline_post -d \
'name=Test&email=test1234@gmail.com&content=This is a test message.' | jq -r '.id')

# Check if the post was added
curl -X GET http://localhost:5000/api/timeline_post

# Delete the corressponding test post request
curl -X DELETE http://localhost:5000/delete/$post_id