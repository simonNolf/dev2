import user
import time


class Register:
    def __init__(self):
        pass

    def register(self):
        while True:
            username = input("New username: ")
            if not len(username) > 0:
                print("Username can't be blank")
                continue
            else:
                break
        while True:
            password = input("New password: ")
            if not len(password) > 0:
                print("Password can't be blank")
                continue
            else:
                break
        role = "user"

        print("Creating account...")
        new_user = user.User(username, password, role)
        new_user.addusers()
        print(new_user.username())
        time.sleep(1)
        print()
        print("Account has been created")

    def encrypt(self, password):
        pass

    def send(self, username, password, role):
        pass