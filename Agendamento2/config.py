import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SAMPLE_SPREADSHEET_ID = '13ZzVX9e9f3iY9aWbVjZ3MLF1GMLX6E36bN__lrfH66A'
SAMPLE_RANGE_NAME = "1!A1:D"  # Assegure-se que 'Sheet1' é o nome correto da aba

def get_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
    return build('sheets', 'v4', credentials=creds)

def adicionar(service, data, hora, paciente, medico):
    valores_adicionar = [[data, hora, paciente, medico]]  # Note o duplo colchete
    try:
        sheet = service.spreadsheets()
        result = sheet.values().append(
            spreadsheetId=SAMPLE_SPREADSHEET_ID,
            range=SAMPLE_RANGE_NAME,
            valueInputOption="RAW",
            body={"values": valores_adicionar}
        ).execute()
        print("Dados adicionados: ", result)
    except Exception as e:
        print("Erro ao adicionar dados: ", e)

# No arquivo principal, ao invocar 'adicionar', você precisa primeiro obter o 'service':
# service = config.get_service()
# config.adicionar(service, data, hora, paciente, medico)