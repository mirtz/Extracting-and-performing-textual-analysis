from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build

# Define the scopes for accessing Google Drive
SCOPES = ['https://www.googleapis.com/auth/drive']

# Path to your credentials JSON file
CREDENTIALS_FILE = '"C:/Users/Mirthula/Downloads/client_secret_962289836358-298ervkavsim2vhg0f5k4r89a7fl5qm9.apps.googleusercontent.com.json".json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE, SCOPES)
service = build('drive', 'v3', credentials=credentials)
