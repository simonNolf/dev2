import time


class User:

    def __init__(self, username='simon', password='simon', role='admin'):
        self.__username = username
        self.__password = password
        self.__role = role
# faire les setter des différents arguments
    def username(self):
        return self.__username

    def password(self):
        return self.__password

    def role(self):
        return self.__role


# Form validation
def validate(form):
    return len(form) > 0


# Login authorization
def loginauth(username, password):

    if User().username() == username:
        if password == User().password():
            print("Login successful")
            return True
    return False


# Login
def login():
    print(User().username())
    print(User().password())
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

    if loginauth(username, password):
        return session(username)
    else:
        print("Invalid username or password")


# Register
def register():
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
    while True:
        role = "user"
        break
    print("Creating account...")
    test = User(username, password, role).password()
    print(test)
    time.sleep(1)
    print()
    print("Account has been created")


# User session
def session(username):
    print("Welcome to your account " + username)
    if User().role() == "admin":
        print("vous avez le role " + User().role())
    while True:
        option = input(username + " > ")
        if option == "logout":
            print("Logging out...")
            break
        elif option == "delete account":
            print("Whos account would you like to delete?")
            userinfo = input("> ")
            if userinfo in User:
                print("Are you sure you want to delete " + userinfo + "'s account?")
                print("Options: yes | no")
                while True:
                    confirm = input("> ")
                    if confirm == "yes":
                        print("Deleting " + userinfo + "'s account...")
                        del User[userinfo]
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


# On start
print("Welcome to the system. Please register or login.")
print("Options: register | login | exit")
while True:
    option = input("> ")
    if option == "login":
        login()
    elif option == "register":
        register()
    elif option == "exit":
        break
    else:
        print(option + " is not an option")

# On exit
print("Shutting down...")
time.sleep(1)
