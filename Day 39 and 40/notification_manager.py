from twilio.rest import Client
import smtplib


# This class is responsible for sending notifications with the deal flight details.
class NotificationManager:
    def send_sms(self, sms):
        account_sid = 'example'
        auth_token = 'example'
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                    body=sms,
                    from_='example',
                    to='example'
            )
        print(message.status)

    def send_emails(self, emails_list, message):
        my_email = 'example'
        my_password = 'example'
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            for email in emails_list:
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=f'Subject:Low price alert!\n\n{message}'
                )
