import smtplib
from datetime import datetime
import pandas
from random import randint


my_email = 'example@email.com'
my_password = 'password'

today = (datetime.now().day, datetime.now().month)
all_persons = pandas.read_csv('birthdays.csv').to_dict(orient='records')

for person in all_persons:
    person_birthday = (person['day'], person['month'])
    if person_birthday == today:
        with open(f'letter_templates/letter_{randint(1, 3)}.txt', 'r') as file:
            letter = file.read().replace('[NAME]', person['name'])
            print(letter)

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=person['email'],
                msg=f'Subject:Happy Birthday!\n\n{letter}'
            )
