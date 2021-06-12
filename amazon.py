import requests
from bs4 import BeautifulSoup
import smtplib
import csv
import datetime
import os

url = input("Enter the url")
pricel = input("Enter the target price")
pricel = int(pricel)

headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68'}

def check_phone_price():
    page = requests.get(url, headers=headers)
    bs = BeautifulSoup(page.content, 'html.parser')
    #print (bs.prettify().encode("utf-8"))
    product_title = bs.find(id= "productTitle").get_text()
    print(product_title.strip())
    price = bs.find(id="priceblock_ourprice").get_text()
    print (price)

    price = price[2:9]
    print (price)

    price_float = float(price.replace(",", ""))
    print (price_float)

    file_exists = True

    if not os.path.exists("./price.csv"):
        file_exists = False


    with open("price.csv","a") as file:
        writer = csv.writer(file, lineterminator='\n')
        fields = ["Timestamp", "Price(Rupees)"]
        if not file_exists:
            writer.writerow(fields)

        timestamp = f"{datetime.datetime.date(datetime.datetime.now())} , {datetime.datetime.time(datetime.datetime.now())}"
        writer.writerow([timestamp, price_float])
        print("wrote data to file")




    return price_float



def send_email():
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(' "your email" ', " email password ")

    subject = "Hey! Drop in price. Are you still interested?"
    body = f"Hello, The prices have been slashed down for the item you selected. Don't lose this wonderful opportunity. Go order now before the price is up again using the following link\n Link: {url} "
    msg = f"Subject: {subject}\n\n\n{body}"

    server.sendmail('vishal.raina@somaiya.edu', 'vishal.raina@somaiya.edu',msg)
    print("email sent")
    server.quit()

price = check_phone_price()
if(price < pricel):
    send_email()

