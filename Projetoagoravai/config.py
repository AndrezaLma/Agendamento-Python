import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '13ZzVX9e9f3iY9aWbVjZ3MLF1GMLX6E36bN__lrfH66A'
SAMPLE_RANGE_NAME = "1!A1:C12"


def main():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)

        service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    # Ler informações do Google Sheets
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    print(values)

    if not values:
        print("No data found.")
        return

    # adicionar/editar valores no Google Sheets
    valores_adicionar = [
        ["Dezembro", "R$ 70.000,00"],
        ["Janeiro/22", "R$80.000,00"],
        ["Fevereiro/22", "R$127.352,00"],
    ]
    result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                   range=SAMPLE_RANGE_NAME, valueInputOption="RAW",
                                   body={"values": valores_adicionar}).execute()

    print(result)
if __name__ == "__main__":
    main()