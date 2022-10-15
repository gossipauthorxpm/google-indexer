import googleapiclient.errors
from googleapiclient.errors import HttpError
from datetime import datetime
from googleapiclient.errors import *


class Indexation:
    accepted_urls: list = list()

    def __init__(self, account):
        self.account = account
        self.account_service = self.account.auth()

    @property
    def get_accepted_urls(self):
        return self.accepted_urls

    def clear_accepted_urls(self):
        self.accepted_urls = list()

    def worker(self, _urls, _method):
        """Отправка url адресов в Google"""
        for url in _urls:
            try:
                content = self.account_service.urlNotifications().publish(
                    body={"url": url, "type": _method}
                ).execute()
                self.accepted_urls.append(url)
                print(f"{datetime.now().replace(microsecond=0)}. Ссылка {url} успешно проиндексирована")
                continue
            except HttpError as error:
                if error.error_details[0]["reason"].__eq__("RATE_LIMIT_EXCEEDED"):
                    return False
                else:
                    print("Ошибка GoogleIndex:\n" + str(error))
            except ConnectionResetError as error:
                print(f"Разрыв соединения с сервером:\n{str(error)}"
                      f"\nПовторная попытка подключения.")
            except Error as error:
                print(f"Ошибка соединения с сервером:\n{str(error)}"
                      f"\nПовторная попытка подключения.")
