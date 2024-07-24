# Install and import 'requests'
import requests

# Get and print out the response from this URL https://jsonplaceholder.typicode.com/photos/1
response = requests.get("https://jsonplaceholder.typicode.com/photos/1")
print(response)

# Print out the title and thumbnail url of the photo from the response
response_json = response.json()
print(response_json["title"])
print(response_json["thumbnailUrl"])