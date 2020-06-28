#!/usr/bin/env python3.8
from accountcredential import Accountcredential
def create_accountcredential(account,username,password):

    new_accountcredential = Accountcredential(account,username,password)
    return new_accountcredential

def save_accountcredentials(accountcredential):
    accountcredential.save_accountcredential()

def del_accountcredential(accountcredential):
    accountcredential.delete_accountcredential()

def find_accountcredential(number):
    return Accountcredential.find_by_number(number)

def check_existing_accountcredentials(number):
    return Accountcredential.accountcredential_exist(number)

def display_accountcredentials():
    return Accountcredential.display_accountcredentials()

def copy_email(number):
        return Accountcredential.accountcredential_found()

def main():
        print("Hello Welcome to your accountcredential list. What is your name?")
        user_name = input()

        print(f"Hello {user_name}. what would you like to do?")
        print('\n')

        while True:
                print("Use these short codes : ca - create a new accountcredential, da - display accountcredentials, fa -find a accountcredential, ex -exit the accountcredential list ")

                short_code = input().lower()

                if short_code == 'cc':
                        print("New Accountcredential")
                        print("-"*10)

                        print ("Account type ....")
                        account = input()

                        print("Username ...")
                        username = input()

                        print("Password ...")
                        password = input()


                        save_accountcredentials(create_accountcredential(account,username,password)) # create and save new accountcredential.
                        print ('\n')
                        print(f"New Accountcredential {account} {username} created")
                        print ('\n')

                elif short_code == 'da':

                        if display_accountcredentials():
                                print("Here is a list of all your accountcredentials")
                                print('\n')

                                for accountcredential in display_accountcredentials():
                                        print(f"{accountcredential.account} {accountcredential.username} .....{accountcredential.password}")

                                print('\n')
                        else:
                                print('\n')
                                print("You dont seem to have any account credentials saved yet")
                                print('\n')

                elif short_code == 'fa':

                        print("Enter the account you want to search for")

                        search_account = input()
                        if check_existing_accountcredentials(search_account):
                                search_accountcredential = find_accountcredential(search_account)
                                print(f"{search_accountcredential.username} {search_accountcredential.password}")
                                print('-' * 20)

                                print(f"Username.......{search_accountcredential.phone_number}")
                                print(f"Password.......{search_accountcredential.email}")
                        else:
                                print("That accountcredential does not exist")

                elif short_code == "ex":
                        print("Bye .......")
                        break
                else:
                        print("I really didn't get that. Please use the short codes")

        if __name__ == '__main__':
                main()