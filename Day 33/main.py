import requests
from datetime import datetime
import time
LAT = 52.268038
LNG = 21.022262


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if LAT-5 <= iss_latitude <= LAT+5 and LNG-5 <= iss_longitude <= LNG+5:
        return True
    else:
        return False


def is_night():
    parameters = {
        'lat': LAT,
        'lng': LNG,
        'formatted': 0

    }
    response = requests.get('https://api.sunrise-sunset.org/json', parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']
    sunrise_h = int(sunrise.split('T')[1].split(':')[0])
    sunset_h = int(sunset.split('T')[1].split(':')[0])
    time_now = datetime.now().hour

    if time_now >= sunset_h or time_now <= sunrise_h:
        return True
    else:
        return False


is_iss_near = False
while not is_iss_near:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        print('Look Up :) The ISS is above you in the sky.')
        is_iss_near = True
