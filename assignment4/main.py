import urllib.request
from bs4 import BeautifulSoup


url = "http://py4e-data.dr-chuck.net/known_by_Naomi.html"

for i in range(7):
    with urllib.request.urlopen(url) as response:
        html = response.read()

    soup = BeautifulSoup(html, "html.parser")

    # Find all the <a> tags in the parsed HTML
    links = soup.find_all("a")
    url = links[17].get("href", None)
    print(links[17].contents[0])
