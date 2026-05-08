from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

query = "being good and evil"
url = f"https://www.amazon.com/s?k={query.replace(' ', '+')}"
driver.get(url)

time.sleep(5)

products = driver.find_elements(By.CSS_SELECTOR, "div.s-result-item[data-component-type='s-search-result']")

data = []

for product in products[:10]:
    try:
        title = product.find_element(By.CSS_SELECTOR, "h2 span").text
    except:
        title = None

    try:
        product_link = product.find_element(By.CSS_SELECTOR, "div a").get_attribute("href")
    except:
        product_link = None

    try:
        image = product.find_element(By.CSS_SELECTOR, "img.s-image").get_attribute("src")
    except:
        image = None

    try:
        price_whole = product.find_element(By.CSS_SELECTOR, ".a-price-whole").text
        price_fraction = product.find_element(By.CSS_SELECTOR, ".a-price-fraction").text
        price = price_whole + "." + price_fraction
    except:
        price = None

    try:
        stars = product.find_element(By.CSS_SELECTOR, ".a-icon-alt").get_attribute("innerHTML")
    except:
        stars = None

    try:
        reviews = product.find_element(By.CSS_SELECTOR, "span.a-size-base.s-underline-text").text
    except:
        reviews = None

    if title:
        data.append({
            "title": title,
            "price": price,
            "image": image,
            "product_link": product_link,
            "stars": stars,
            "reviews": reviews
        })

driver.quit()

for item in data:
    print("Titre:", item["title"])
    print("Prix:", item["price"])
    print("Image:", item["image"])
    print("Lien:", item["product_link"])
    print("Stars:", item["stars"])
    print("Reviews:", item["reviews"])
    print("-" * 50)