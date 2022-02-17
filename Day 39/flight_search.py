import requests
from flight_data import FlightData


# This class is responsible for talking to the Flight Search API.
class FlightSearch:
    def __init__(self):
        self.url = 'https://tequila-api.kiwi.com'
        self.api_key = 'key_example'
        self.headers = {'apikey': self.api_key}

    def get_destination_code(self, city_name):
        location_endpoint = f'{self.url}/locations/query'
        params = {
            'term': city_name,
            'location_types': 'city'
        }
        response = requests.get(url=location_endpoint, headers=self.headers, params=params)
        result = response.json()['locations']
        code = result[0]['code']
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        search_endpoint = f'{self.url}/v2/search'
        params = {
            'fly_from': origin_city_code,
            'fly_to': destination_city_code,
            'date_from': from_time.strftime("%d/%m/%Y"),
            'date_to': to_time.strftime("%d/%m/%Y"),
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 14,
            'flight_type': 'round',
            'one_for_city': 1,
            'max_stopovers': 0,
            'curr': 'USD'
        }
        response = requests.get(url=search_endpoint, headers=self.headers, params=params)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data
