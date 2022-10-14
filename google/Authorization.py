from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class Authorization:
    def __init__(self, file_path):
        """
        Авторизация в сервисы гугл
        """
        self.OAUTH_FILE_PATH = file_path
        self.SCOPES = ["https://www.googleapis.com/auth/indexing"]
        self.SERVICE_NAME = 'indexing'
        self.VERSION = "v3"

    def auth(self):
        flow = InstalledAppFlow.from_client_secrets_file(self.OAUTH_FILE_PATH, self.SCOPES)
        credentials = flow.run_local_server(port=0)

        try:
            service = build(self.SERVICE_NAME, self.VERSION,
                            credentials=credentials, cache_discovery=False)
            return service


        except HttpError as error:
            print("Ошибка подключения к сервисам Google:\n" + str(error))
