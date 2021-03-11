import requests
from bs4 import BeautifulSoup


URL = 'https://www.amazon.co.uk/PlayStation-9395003-5-Console/dp/B08H95Y452/ref=sr_1_1?dchild=1&keywords=ps5&qid=1615488436&sr=8-1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

def check_availability():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    availability = soup.find(id="availability").get_text()

    if 'unavailable' not in availability:
        send_mail()

    print(availability.strip())
    print(title.strip())