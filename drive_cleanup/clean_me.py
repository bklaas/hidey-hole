import os
import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Replace with the path to your service account key file
SERVICE_ACCOUNT_FILE = 'path/to/your/service-account-file.json'
SCOPES = ['https://www.googleapis.com/auth/drive']

# Replace with your folder ID
FOLDER_ID = 'YOUR_FOLDER_ID'

def get_drive_service():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return build('drive', 'v3', credentials=credentials)

def list_files_in_folder(service, folder_id):
    try:
        results = service.files().list(
            q=f"'{folder_id}' in parents and mimeType='application/vnd.google-apps.spreadsheet' and trashed=false",
            fields="nextPageToken, files(id, name, modifiedTime)"
        ).execute()
        return results.get('files', [])
    except HttpError as error:
        print(f'An error occurred: {error}')
        return []

def move_to_trash(service, file_id):
    try:
        service.files().update(fileId=file_id, body={'trashed': True}).execute()
        print(f'Moved to trash: {file_id}')
    except HttpError as error:
        print(f'An error occurred: {error}')

def main():
    service = get_drive_service()
    files = list_files_in_folder(service, FOLDER_ID)
    two_months_ago = datetime.datetime.now() - datetime.timedelta(days=60)

    for file in files:
        modified_time = datetime.datetime.fromisoformat(file['modifiedTime'][:-1])
        if modified_time < two_months_ago:
            move_to_trash(service, file['id'])

if __name__ == '__main__':
    main()

