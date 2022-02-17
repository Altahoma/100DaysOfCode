from twilio.rest import Client


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
        pass
