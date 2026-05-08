import requests
from bs4 import BeautifulSoup

query = "iphone 13"

url = f"https://www.jumia.ma/catalog/?q={query.replace(" ","+")}"

response = requests.get(url)

html = response.text

soup = BeautifulSoup(html, "html.parser")


products = soup.find_all("a", class_="core")

print(products[0])
print(type())


for product in products:
    print(type(product))
    try:
        product_link = product["href"]
    except:
        product_link = None

    try:
        product_img_link = product.find("img", class_="img")["data-src"]
    except:
        product_img_link = None

product_link = soup.find("a", class_="core")["href"]
product_img_link = soup.find("img", class_="img")["data-src"]
product_title = soup.find("h3", class_="name").text
product_price = soup.find("div", class_="prc").text


print(product_link)
print(product_img_link)
print(product_title)
print(product_price)