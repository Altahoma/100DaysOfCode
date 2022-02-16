import requests
import datetime as dt


username = 'example_username'
token = 'example_token'
url = 'https://pixe.la'

# Create new user
pixela_endpoint = f'{url}/v1/users'
user_config = {
    'token': token,
    'username': username,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
# response = requests.post(url=pixela_endpoint, json=user_config)
# print(response.text)

# Create graph
graph_endpoint = f'{pixela_endpoint}/{username}/graphs'
graph_id = 'reading'
graph_config = {
    'id': graph_id,
    'name': 'Reading Graph',
    'unit': 'pages',
    'type': 'int',
    'color': 'ajisai'
}
headers = {
    'X-USER-TOKEN': token
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Post a pixel
pixel_endpoint = f'{graph_endpoint}/{graph_id}'
today = dt.datetime.today().strftime('%Y%m%d')
page_qt = input('How many pages did you read today?: ')
pixel_config = {
    'date': today,  # yyyyMMdd format
    'quantity': page_qt
}
# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

# Update a pixel
update_endpoint = f'{pixel_endpoint}/{today}'
page_qt = input('Enter count of pages to update: ')
update_config = {
    'quantity': page_qt
}
# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)

# Delete a pixel
delete_endpoint = f'{pixel_endpoint}/{today}'
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)

# Delete a user
delete_user = f'{pixela_endpoint}/{username}'
# response = requests.delete(url=delete_user, headers=headers)
# print(response.text)