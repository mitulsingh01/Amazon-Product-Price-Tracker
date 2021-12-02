import requests
from bs4 import BeautifulSoup
import smtplib

BUY_PRICE = 100000
EMAIL = "mitulsingh182@gmail.com"
PASSWORD = "abc@3182"
url = "https://www.amazon.in/dp/B08L5V1SBB/?pf_rd_r=TBR1PZQWF82WK763FZNP&pf_rd_p=3e9a1841-acb2-4cb1-b49f-a7f195b94d05&pd_rd_r=f201ac6f-5283-41b4-92c5-368705589f3c&pd_rd_w=hXrf7&pd_rd_wg=HH40b&ref_=pd_gw_unk"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
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
    message = f"Hey Mitul, you can now buy your favourite phone for {price}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject: Amazon Price Alert! \n\n {message} \n {url}"
        )



