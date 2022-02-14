import requests
from twilio.rest import Client


def take_umbrella(json_data):
    next_12_hours = json_data['hourly'][:12]
    for hour in next_12_hours:
        weather_code = hour['weather'][0]['id']
        if weather_code < 700:
            return True


url = 'https://api.openweathermap.org/data/2.5/onecall'
params = {
    'lat': 60,
    'lon': 10,
    'appid': 'appid_example',
    'exclude': 'current,minutely,daily,alerts'
}

response = requests.get(url, params)
response.raise_for_status()
data = response.json()

if take_umbrella(data):
    account_sid = 'TWILIO_ACCOUNT_SID'
    auth_token = 'TWILIO_AUTH_TOKEN'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
                body="It's raining bro ☔️",
                from_='+15017122661',
                to='+15558675310'
        )

    print(message.status)
