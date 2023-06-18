import urllib.request
from bs4 import BeautifulSoup


url = "http://py4e-data.dr-chuck.net/comments_1838539.html"
with urllib.request.urlopen(url) as response:
    html = response.read()


soup = BeautifulSoup(html, "html.parser")
tags = soup("span")

numbers = [int(tag.contents[0]) for tag in tags]
sum = sum(numbers)

print(sum)
