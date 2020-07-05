#!/usr/bin/env python3.8
from accountcredential import Accountcredential
def create_accountcredential(account,username,password):

    new_accountcredential = Accountcredential(account,username,password)
    return new_accountcredential

def save_accountcredential(accountcredential):
    accountcredential.save_accountcredential()

def del_accountcredential(accountcredential):
    accountcredential.delete_accountcredential()

def find_accountcredential(username):
    return Accountcredential.find_by_username(username)

def check_existing_accountcredential(username):
    return Accountcredential.accountcredential_exist(username)

def display_accountcredential():
    return Accountcredential.display_accountcredential(accountcredential)

def main():
    print("Hello Welcome to your accountcredential list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : ca - create a new accountcredential, da - display accountcredential, fa -find an accountcredential, ex -exit the accountcredential list ")

        short_code = input().lower()

        if short_code == 'ca':
                print("New Accountcredential")
                print("-"*10)

                print ("Account ....")
                accountentry = input()

                print("Username ...")
                usernameentry = input()

                print("Password ...")
                passwordentry = input()

                save_accountcredential(create_accountcredential(accountentry,usernameentry,passwordentry)) # create and save new accountcredential.
                print ('\n')
                print(f"New Accountcredential {accountentry} for {usernameentry} created")
                print ('\n')

        elif short_code == 'da':

                if display_accountcredential():
                        print("Here is a list of all your accountcredentials")
                        print('\n')

                        for accountcredential in display_accountcredential():
                                print(f"{accountcredential.first_name} {accountcredential.last_name} .....{accountcredential.phone_number}")

                                print('\n')
                else:
                        print('\n')
                        print("You dont seem to have any accountcredentials saved yet")
                        print('\n')

        elif short_code == 'fa':

                print("Enter the number you want to search for")

                search_account = input()
                if check_existing_accountcredential(search_account):
                        search_accountcredential = find_accountcredential(search_account)
                        print(f"{search_accountcredential.account} {search_accountcredential.username}")
                        print('-' * 20)

                        print(f"Phone number.......{search_accountcredential.phone_number}")
                        print(f"Email address.......{search_accountcredential.email}")
                else:
                        print("That accountcredential does not exist")

        elif short_code == "ex":
                print("Bye .......")
                break
        else:
                print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
        main()