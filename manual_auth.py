import os
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.send']
creds = None

try:
    # Load credentials
    if os.path.exists('token.json'):
        creds = google.auth.load_credentials_from_file('token.json', SCOPES)
        print("Loaded credentials from token.json")

    # If no valid credentials, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
            print("OAuth flow completed")

        with open('token.json', 'w') as token:
            token.write(creds.to_json())
            print("Token stored successfully")
except Exception as e:
    print(f"An error occurred: {e}")
