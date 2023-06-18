import json
import urllib.request

# Prompt for a URL
url = "http://py4e-data.dr-chuck.net/comments_1838542.json"

# Read the JSON data from the URL
response = urllib.request.urlopen(url)
data = response.read().decode()

# Parse the JSON data
info = json.loads(data)

# Initialize a variable to hold the sum of the comment counts
total_count = 0

# Loop through the comments and add up the counts
for item in info["comments"]:
    count = int(item["count"])
    total_count += count

# Print the total count
print("Total count:", total_count)
