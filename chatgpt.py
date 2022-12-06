
import requests

url = 'https://adventofcode.com/2022/day/4'

# Create a session object to identify yourself on the page
headers = {'User-Agent': 'doraani (https://github.com/doraani)'}

# Make an HTTP GET request
response = requests.get(url, headers=headers)

# Get the content of the page
content = response.content

# Write the content to the file
with open('day4.txt', 'wb') as f:
    f.write(content)