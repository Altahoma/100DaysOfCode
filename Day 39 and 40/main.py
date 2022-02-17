# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

ORIGIN_CITY_IATA = "IEV"


data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

data_manager.add_new_user()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
sheet_data = data_manager.read_table('cities')

for index, country_data in enumerate(sheet_data[1:]):
    row = index + 2
    city_name = country_data[0]
    city_code = flight_search.get_destination_code(city_name)
    min_price = country_data[2]
    data_manager.write_country_code(row, city_code)

    ticket = flight_search.check_flights(ORIGIN_CITY_IATA, city_code, tomorrow, six_month_from_today)

    if ticket is None:
        continue

    if int(min_price) > ticket.price:
        title = 'Low price alert!'
        message = f'Only ${ticket.price} to fly from {ticket.origin_city}-{ticket.origin_airport}' \
                  f' to {ticket.destination_city}-{ticket.destination_airport}, from {ticket.out_date}' \
                  f' to {ticket.return_date}.'
        notification_manager.send_sms(f'{title} {message}')
        emails_list = [email[2] for email in data_manager.read_table('users')[1:]]
        notification_manager.send_emails(emails_list, message)

