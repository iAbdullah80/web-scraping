import requests
from bs4 import BeautifulSoup
import smtplib
import time, sys

URl = 'https://www.extra.com/en-sa/mobiles-tablets/mobiles/smartphone/apple-iphone-12-pro-5g-128gb-pacific-blue/p/100203659'
URL2 = 'https://www.jarir.com/sa-en/catalog/product/view/id/297650/category/1785/'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

def check_availability_extra():
    page = requests.get(URl, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(id="addToCartForm").get_text()
    availability = price.strip()[:11]
    not_available = "Notify Me"
    available = "Add To Cart"

    if available in availability:
        send_mail_extra()
    if not_available in availability:
        check_availability_jarir()

def check_availability_jarir():
    page = requests.get(URL2, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find('div', {"class":"add-to-cart__button"}).get_text()
    availability = price.strip()[:20]
    not_available = "Not Available Online"
    available = "Add to Cart"

    if available in availability:
        send_mail_jarir()
    if not_available in availability:
        for i in range(7):
            sys.stdout.write("   ")
            x = i % 4
            sys.stdout.write('\r' + "." * x)
            time.sleep(0.5)
            sys.stdout.flush()
    check_availability_extra()


def send_mail_extra():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('thy5abdullah@gmail.com', 'penfpoolerzhtmjn')
    subject = "The iPhone 12 Pro is AVAILABLE!"
    body = 'Check the eXtra Store link: https://www.extra.com/en-sa/mobiles-tablets/mobiles/smartphone/apple-iphone-12-pro-5g-128gb-pacific-blue/p/100203659'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'thy5abdullah@gmail.com',
        ['thyabdullah@gmail.com','azaoi1000@gmail.com'],
        msg
    )
    print("HEY EXTRA STORE EMAIL HAS BEEN SENT!")
    server.quit()

def send_mail_jarir():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('thy5abdullah@gmail.com', 'penfpoolerzhtmjn')
    subject = "The iPhone 12 Pro is AVAILABLE!"
    body = 'Check the Jarir Store link: https://www.jarir.com/sa-en/catalog/product/view/id/297650/category/1785/'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'thy5abdullah@gmail.com',
        ['thyabdullah@gmail.com','azaoi1000@gmail.com'],
        msg
    )
    print("HEY JARIR EMAIL HAS BEEN SENT!")
    server.quit()
check_availability_extra()