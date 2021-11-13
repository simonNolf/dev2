import time

import user

class Login:
    def __init__(self):
        pass

    def loginauth(self,username, password):
        if user.User().username() == username:
            if password == user.User().password():
                print("Login successful")
                return True
        return False


    # Login
    def login(self):
        while True:
            username = input("Username: ")
            if not len(username) > 0:
                print("Username can't be blank")
            else:
                break
        while True:
            password = input("Password: ")
            if not len(password) > 0:
                print("Password can't be blank")
            else:
                break

        if self.loginauth(self, username, password):
            return self.session(username)
        else:
            print("Invalid username or password")


    def session(self,username):
        print("Welcome to your account " + username)
        if user.User().role() == "admin":
            print("vous avez le role " + user.User().role())
        while True:
            option = input(username + " > ")
            if option == "logout":
                print("Logging out...")
                break
            elif option == "delete account":
                print("Whos account would you like to delete?")
                userinfo = input("> ")
                if userinfo in user.User:
                    print("Are you sure you want to delete " + userinfo + "'s account?")
                    print("Options: yes | no")
                    while True:
                        confirm = input("> ")
                        if confirm == "yes":
                            print("Deleting " + userinfo + "'s account...")
                            del user.User[userinfo]
                            time.sleep(1)
                            print(userinfo + "'s account has been deleted")
                            break
                        elif confirm == "no":
                            print("Canceling account deletion...")
                            time.sleep(1)
                            print("Account deletion canceled")
                            break
                        else:
                            print(confirm + " is not an option")
                else:
                    print("There is no account with that username")
            else:
                print(option + " is not an option")
