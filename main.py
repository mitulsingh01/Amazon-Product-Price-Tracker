import requests
from bs4 import BeautifulSoup
import smtplib

BUY_PRICE = Your price
EMAIL = "Your Email"
PASSWORD = "Your Password"
url = "URL for your product"
headers = {
    "User-Agent": "User-Agent",
    "Accept-Language": "Accepted Languages",
}
response = requests.get(url, headers=headers).text
soup = BeautifulSoup(response, "lxml")
infoProduct = soup.find('div', id="unifiedPrice_feature_div" ,class_="celwidget")
title = soup.find('span', id="productTitle", class_="a-size-large product-title-word-break")
if title:
    title = title.get_text()
else:
    title = "default_title"
print(title)
price = infoProduct.find('span', class_="a-size-medium a-color-price priceBlockBuyingPriceString")
price = price.get_text().strip("₹")
price = price.replace(",", "")
print(price)

if int(float(price)) < BUY_PRICE:
    message = f"Hey User, you can now buy your favourite phone for {price}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject: Amazon Price Alert! \n\n {message} \n {url}"
        )



