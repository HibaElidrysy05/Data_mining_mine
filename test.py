import requests
from bs4 import BeautifulSoup

html = """<a class ="accueil-link" href="#">Accueil</a>"""

soup = BeautifulSoup(html,"html.parser")

link = soup.find("a", class_="accueil-link")


print(link)
print(link.text)
print(link["href"])