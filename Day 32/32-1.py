import smtplib
import datetime as dt
from random import choice


my_email = 'example@email.com'
my_password = 'password'

now = dt.datetime.now()
if now.weekday() == 0:
    with open('quotes.txt', 'r') as file:
        quotes = file.readlines()
    quote = choice(quotes)
    print(quote)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='example2@email.com',
            msg=f'Subject:Good Monday!\n\n{quote}'
        )
