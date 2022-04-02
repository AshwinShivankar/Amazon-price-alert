from bs4 import BeautifulSoup
import lxml
import requests
import smtplib


my_email = "ashwin.shv21@gmail.com"
password = "Python@21"



headers = { 'Accept-Language' : "en-GB,en-US;q=0.9,en;q=0.8",
            'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
response = requests.get(url="https://www.amazon.in/Boat-Stone-1000-Bluetooth-Monstrous/dp/B072PQRS12/ref=sr_1_4?crid=3OGV2XBT7SUMY&keywords=boat%2Bbluetooth%2Bspeaker&qid=1643710462&sprefix=boat%2B%2Caps%2C354&sr=8-4&th=1",
                        headers=headers)
web_page = response.content
soup = BeautifulSoup(web_page, "lxml")
try:
    global prices

    prices = soup.find( name="span", class_="a-offscreen").get_text()
    # price_without_currency = prices.split("₹")[1]
    # prices_int = float(price_without_currency)
    print(prices)

except AttributeError:
    print("try again")


PRICE = '2000'


if prices < PRICE:
    connection= smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(my_email, password )
    connection.sendmail(
         from_addr=my_email,
         to_addrs=my_email,
         msg=f"Subject:Amazon Price Alert!"
        )






