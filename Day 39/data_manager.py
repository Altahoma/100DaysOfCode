from googleapiclient.discovery import build
from google.oauth2 import service_account


# This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.sheet_name = 'cities'
        scopes = ['https://www.googleapis.com/auth/spreadsheets']
        service_account_file = 'keys_example.json'
        creds = service_account.Credentials.from_service_account_file(service_account_file, scopes=scopes)
        self.service = build('sheets', 'v4', credentials=creds)
        self.spreadsheet_id = 'spreadsheet_id_example'
        self.table_range = f'{self.sheet_name}!A:C'
        self.sheet = self.service.spreadsheets()

    def read_table(self):
        result = self.sheet.values().get(spreadsheetId=self.spreadsheet_id, range=self.table_range).execute()
        values = result.get('values', [])
        return values

    def write_country_code(self, row, code):
        range_update = f'{self.sheet_name}!B{row}'
        request = self.service.spreadsheets().values().update(spreadsheetId=self.spreadsheet_id, range=range_update,
                                                              valueInputOption='USER_ENTERED',
                                                              body={'values': [[code]]})
        request.execute()
