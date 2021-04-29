import os
import smtplib
import time

import requests
from bs4 import BeautifulSoup


def check_availability(url, headers):
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    TITLE = soup.find(id="productTitle").get_text()
    AVAILABILITY = soup.find(id="availability").get_text()

    if 'unavailable' in AVAILABILITY:
        send_mail()
    else:
        print(f"{TITLE.strip()} is out of stock.")


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()
    server.starttls()
    server.ehlo()

    from_email = os.environ.get('FROM_EMAIL_USER')
    from_email_password = os.environ.get('FROM_EMAIL_PASS')
    to_email = os.environ.get('TO_EMAIL_USER')

    server.login(from_email,
                 from_email_password)

    subject = "Item is back in stock!"
    body = "Check the Amazon link:\n\nhttps://www.amazon.co.uk/PlayStation-9395003-5-Console/dp/B08H95Y452/ref=sr_1_1?dchild=1&keywords=ps5&qid=1615488734&sr=8-1"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        from_email,
        to_email,
        msg
    )
    print('EMAIL HAS BEEN SENT!')

    server.quit()


while True:
    check_availability('https://www.amazon.co.uk/PlayStation-9395003-5-Console/dp/B08H95Y452/ref=sr_1_1?dchild=1&keywords=ps5&qid=1615488436&sr=8-1',
                       {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'})
    time.sleep(60)
