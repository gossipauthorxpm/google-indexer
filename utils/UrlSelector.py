import os


class UrlSelector:
    """Управление файлом с ссылками"""

    def __init__(self, delete_links):
        self.__get_links()
        self.urls_list = self.__clear_empty_links("\n")
        if delete_links is True:
            self.__delete_links()

    urls_list: list = list()
    path_file = "./urls-list.txt"
    path_accepted_file = "./accepted_links.txt"

    @property
    def get_links(self):
        return self.urls_list

    def __get_links(self):
        """Добавляет 200 ссылок из файла"""
        try:
            with open(self.path_file, encoding="UTF-8", mode="r") as file:
                self.urls_list = file.readlines()
                self.urls_list = self.urls_list[:200]
                file.close()
        except IOError as error:
            print("Ошибка открытия со ссылками!:\n" + str(error))

    def __clear_empty_links(self, remove: str):
        for url in range(len(self.urls_list)):
            try:
                self.urls_list.remove(remove)
            except ValueError:
                return self.urls_list

    def __clear_file(self):
        with open(self.path_file, encoding="UTF-8", mode="w"):
            pass

    def __rewrite_file(self, links: list):
        with open(self.path_file, encoding="UTF-8", mode="w") as file:
            file.writelines(links)
            file.close()

    def __delete_links(self):
        """Удаляет ссылки из файла"""
        try:
            with open(self.path_file, encoding="UTF-8", mode="r") as file:
                links = file.readlines()
                # Если ссылок меньше чем 200
                if len(self.urls_list) <= 200 and len(links) <= 200:
                    file.close()
                    self.__clear_file()
                # Если ссылок больше чем 200
                else:
                    no_action_links_file = links[200:]
                    file.close()
                    self.__rewrite_file(no_action_links_file)
        except IOError as error:
            print("Ошибка изменения файла со ссылками!:\n" + str(error))

    def overwriting_links(self, temp_links: list):
        try:
            with open(self.path_file, encoding="UTF-8", mode="a") as file:
                file.writelines(temp_links)
                file.close()
        except IOError as error:
            print("Ошибка изменения файла во время дозаписи:\n" + str(error))

    def write_accepted_links(self, links: list):
        try:
            with open(self.path_accepted_file, encoding="UTF-8", mode="a") as file:
                file.writelines(links)
                file.close()
        except IOError as error:
            print("Ошибка изменения файла с отработанными ссылками:\n" + str(error))


if __name__ == "__main__":
    UrlSelector()
