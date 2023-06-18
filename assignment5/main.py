import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1838541.xml"
print("Retrieving", url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()

print("Retrieved", len(data), "characters")

tree = ET.fromstring(data)

comments = tree.findall(".//comment")

total_count = 0
for comment in comments:
    count = comment.find("count").text
    total_count += int(count)

print("Total:", total_count)
