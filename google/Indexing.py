import time
from datetime import datetime
from googleapiclient.errors import *
from google.GoogleError import GoogleError


class Indexation:
    accepted_urls: list = list()

    def __init__(self, account):
        self.account = account
        self.account_service = self.account.auth()

    @property
    def get_accepted_urls(self):
        return self.accepted_urls

    def set_account(self, account):
        self.account = account

    def clear_accepted_urls(self):
        self.accepted_urls = list()

    def worker(self, _urls, _method):
        """Отправка url адресов в Google"""
        for url in _urls:
            try:
                time.sleep(2)
                content = """{
                  \"url\": \"%s\",
                  \"type\": \"%s\"
                }""" % (url, _method)
                response, content = self.account_service.request(self.account.get_endpoint, method="POST", body=content)
                if response['status'].__eq__("403"):
                    raise GoogleError("Отказано в доступе. Проверьте правильность заполнения доступа аккаунтов сайта(403 error)!")
                elif response['status'].__eq__("200"):
                    self.accepted_urls.append(url)
                    print(f"{datetime.now().replace(microsecond=0)}. Ссылка {url} успешно проиндексирована")
                elif response['status'].__eq__("402"):
                    return False
                elif response['status'].__eq__("429"):
                    raise GoogleError("To many requests(429 error)!")

            except ConnectionResetError as error:
                print(f"Разрыв соединения с сервером:\n{str(error)}"
                      f"\nПовторная попытка подключения.")
            except Error as error:
                print(f"Ошибка соединения с сервером:\n{str(error)}"
                      f"\nПовторная попытка подключения.")
            except GoogleError as error:
                print(f"Ошибка подключения:\n{str(error)}")
                return False, "google_error"
