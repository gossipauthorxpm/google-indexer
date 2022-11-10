class SelectAccount:
    not_valid_accounts = list()

    def __init__(self, accounts, use_account):
        self.accounts = accounts
        self.valid_account = use_account
        self.len_accounts = len(self.accounts)

    @property
    def get_valid_account(self):
        return self.valid_account

    def unvalid_account(self):
        self.not_valid_accounts.append(self.valid_account)
        self.valid_account = self.__get_valid_account()

    def __get_not_used_accounts(self, all_accounts, used_accounts):
        for used_account in used_accounts:
            try:
                index = all_accounts.index(used_account)
                all_accounts.pop(index)
            except ValueError:
                continue
        return all_accounts

    def __check_len_not_valid_accounts(self):
        len_not_valid = len(self.not_valid_accounts)
        if len_not_valid == self.len_accounts:
            return False
        else:
            return True

    def __get_valid_account(self):
        not_used_accounts = self.__get_not_used_accounts(self.accounts, self.not_valid_accounts)

        if not self.check_accounts():
            self.valid_account = self.accounts[0]
        else:
            self.valid_account = not_used_accounts[0]
        return self.valid_account

    def check_accounts(self):
        if not self.__check_len_not_valid_accounts():
            accounts = list(self.not_valid_accounts)
            self.accounts = accounts
            self.not_valid_accounts.clear()
            return False
        else:
            return True
