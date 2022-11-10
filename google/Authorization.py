import httplib2
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials


class Authorization:
    def __init__(self, file_path):
        """
        Авторизация в сервисы гугл
        """
        self.JSON_KEY_FILE = file_path
        self.SCOPES = ["https://www.googleapis.com/auth/indexing"]
        self.ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"

    @property
    def get_endpoint(self):
        return self.ENDPOINT

    def set_file_path(self, file_path):
        self.JSON_KEY_FILE = file_path

    def auth(self):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.JSON_KEY_FILE, scopes=self.SCOPES)

        try:
            http = credentials.authorize(httplib2.Http())
            return http

        except HttpError as error:
            print("Ошибка подключения к сервисам Google:\n" + str(error))
