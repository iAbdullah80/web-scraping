import requests
from bs4 import BeautifulSoup
import smtplib
import time

URl = 'https://www.tadawul.com.sa/wps/portal/tadawul/market-participants/issuers/issuers-directory/company-details/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zi_Tx8nD0MLIy83V1DjA0czVx8nYP8PI0MDAz0I4EKzBEKDEJDLYEKjJ0DA11MjQzcTfXDyzJTy_XDCSkryE4yBQA8k2I6/?companySymbol=6020'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/87.0.4280.88 Safari/537.36'}

def stock_price():

    page = requests.get(URl, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    #title = soup.select('.table_sep')
    #for ti in title:
       # print(ti)
       # print('')
    price_down = soup.find_all('dl', {"class":"in_tbl large down"})
    price = soup.find_all('dl', {"class":"in_tbl large up"})
    for p in price:
        pp = float(p.text[90:96])
        if pp >= 19.02:
            send_mail()
            break
        else:
            break
    for pd in price_down:
        ppd= float(pd.text[90:96])
        if ppd >= 19.02:
            send_mail()
            break
        else:
            stock_price()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('thy5abdullah@gmail.com', 'penfpoolerzhtmjn')
    subject = "GACO is at sell point! 19.20!!!"
    body = 'Check the Tadawl link https://www.tadawul.com.sa/wps/portal/tadawul/market-participants/issuers/issuers-directory/company-details/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zi_Tx8nD0MLIy83V1DjA0czVx8nYP8PI0MDAz0I4EKzBEKDEJDLYEKjJ0DA11MjQzcTfXDyzJTy_XDCSkryE4yBQA8k2I6/?companySymbol=6020'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'thy5abdullah@gmail.com',
        'thyabdullah@gmail.com',
        msg
    )
    print("HEY EMAIL HAS BEEN SENT!!!")
    server.quit()
stock_price()
