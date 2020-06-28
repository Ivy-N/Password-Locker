
class Accountcredential:

    accountcredential_list = [] 

    def __init__(self,account,username,password):

        self.account = account
        self.username = username
        self.password = password

    def save_accountcredentials(self):
        Accountcredential.accountcredential_list.append(self)

    def delete_accountcredentials(self):

      Accountcredential.accountcredential_list.remove(self)

    @classmethod
    def find_by_username(cls,account):

        for accountcredential in cls.accountcredential_list:
            if accountcredential.account == account:
                return accountcredential

    @classmethod
    def accountcredential_exist(cls,account):
        
        for accountcredential in cls.accountcredential_list:
            if accountcredential.account == account:
                    return True

            return False