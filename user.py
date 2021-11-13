import time


class User:
    """
    create a user to access at the platform
    :param username : the username
    :type username : string
    :param password : the password of the user
    :type password : string
    :param role : the role of the user
    :type role : string
    """

    def __init__(self, username, password, role):
        self.__username = username
        self.__password = password
        self.__role = role
        self.__users = []

    # faire les setter des differents arguments
    def username(self):
        return self.__username

    def password(self):
        return self.__password

    def role(self):
        return self.__role

    def addusers(self):
        dico = {}
        dico["username"] = self.__username
        dico["password"] = self.__password
        dico["role"] = self.__role
        self.__users.append(dico)
        print(self.__users)


# Form validation
#def validate(form):
#    return len(form) > 0
