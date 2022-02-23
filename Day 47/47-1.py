import requests
import smtplib
from bs4 import BeautifulSoup


URL = 'product link'
MIN_PRICE = 200


response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')
find_price = soup.find(name='p', class_='product-prices__big')
price = int(find_price.text.strip().replace('₴', ''))
find_title = soup.find(name='h1', class_='product__title')
title = find_title.text.strip()

if price < MIN_PRICE:
    my_email = 'example'
    my_password = 'example'
    message = f'{title}\n' \
              f'Current price = {price}\n' \
              f'{URL}'

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='example',
            msg=f'Subject:Low price alert!\n\n{message}'
        )
