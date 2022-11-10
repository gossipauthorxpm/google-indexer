import os


class DomainSelector:
    """Выбор доменов для добавления/удаления ссылок"""

    def __init__(self):
        self.__check_domains_files()

    @property
    def get_path_account_json(self):
        return self.domains["file_paths"][0]

    @property
    def get_all_accounts(self):
        return self.domains["file_paths"]

    domains: dict = dict({
        "domains": list(),
        "file_paths": list()
    })

    path: str = "./domain_owners"

    def __check_domains_files(self):
        """Проверка папки владельцев ключей и доменов и добавления их в словарь
        структура домен:путь к ключу"""

        try:
            for filename in os.listdir(self.path):
                self.domains["domains"].append(filename)
                self.domains["file_paths"].append(self.path + f"/{filename}")
            if self.domains["domains"] and self.domains["file_paths"] == []:
                print("Папка с ключами владельцев пуста!")
        except os.EX_OSFILE as error:
            print("Произошла ошибка чтения файла:\n" + str(error))
