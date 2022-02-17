from googleapiclient.discovery import build
from google.oauth2 import service_account


# This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.sheets = {'cities': 'A:C', 'users': 'A:C'}
        scopes = ['https://www.googleapis.com/auth/spreadsheets']
        service_account_file = '../api-reader-keys.json'
        creds = service_account.Credentials.from_service_account_file(service_account_file, scopes=scopes)
        self.service = build('sheets', 'v4', credentials=creds)
        self.spreadsheet_id = 'example'

        self.sheet = self.service.spreadsheets()

    def read_table(self, sheet_name):
        table_range = f'{sheet_name}!{self.sheets[sheet_name]}'
        result = self.sheet.values().get(spreadsheetId=self.spreadsheet_id, range=table_range).execute()
        values = result.get('values', [])
        return values

    def write_country_code(self, row, code):
        range_update = f'cities!B{row}'
        request = self.service.spreadsheets().values().update(spreadsheetId=self.spreadsheet_id, range=range_update,
                                                              valueInputOption='USER_ENTERED',
                                                              body={'values': [[code]]})
        request.execute()

    def write_new_user(self, user_info):
        all_users = self.read_table('users')
        row = len(all_users) + 1
        range_update = f'users!A{row}'
        request = self.service.spreadsheets().values().update(spreadsheetId=self.spreadsheet_id, range=range_update,
                                                              valueInputOption='USER_ENTERED',
                                                              body={'values': [user_info]})
        request.execute()

    def add_new_user(self, first_n=None, last_n=None):
        if first_n and last_n:
            first_name = first_n
            last_name = last_n
        else:
            print('Welcome to Flight Club.')
            first_name = input('What is your first name?\n')
            last_name = input('What is your last name?\n')
        email = input('What is your email?\n')
        repeat_email = input('Type your email again.\n')

        if email != repeat_email:
            print('Incorrect email, please try again.')
            self.add_new_user()

        self.write_new_user([first_name, last_name, email])
