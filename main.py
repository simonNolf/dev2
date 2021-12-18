import login as login
import register as register
import time

if __name__ == "__main__":
    # On start
    print("Welcome to the system. Please register or login.")
    print("Options: register | login | exit")
    while True:
        option = input("> ")
        if option == "login":
            login.Login().login()
        elif option == "register":
            register.Register().register()
        elif option == "exit":
            break
        else:
            print(option + " is not an option")

    # On exit
    print("Shutting down...")
    time.sleep(1)
