from crud_authentification import CRUD_authentification
from mysql.connector import Error
import eel

eel.init("web")
eel.start("index.html")


connect = CRUD_authentification()

# def __init__(self):
#     connect = CRUD_authentification()
eel.init("web")
# eel.start("index.html", mode='mozilla',port=9998)


@eel.expose
def Signup(nom: str, prenom: str, email: str, password_hash: str):

    if "" not in [nom, prenom, email, password_hash]:

        for i in connect.read(email):
            try:
                if i[3] != email:
                    connect.create(nom, prenom, email, password_hash)
                    print("ok")
                    return True
            except Error as e:
                print("Il semble y avoir une erreur veuillez réessayer")


@eel.expose
def Signin(email: str, password_hash: str):
    print(password_hash)
    if "" not in [email, password_hash]:
        for i in connect.read(email):
            if i[3] == email and i[4] == password_hash:
                print("connection ok")
                eel.redirect_chat()()


@eel.expose
def get_user_email():
    email = eel.getUserEmail()()
    return email

# def start(self):
#     eel.start("index.html", mode='mozilla',port=9998)


# print( get_user_email())


# print (appel
# print(f"L'adresse2{value}")
# value = None

# @eel.expose
# def get_user_email():
#     email = eel.getUserEmail()
#     return email

# value = eel.getUserEmail()
# print(value)
# get_user_email()
# def get_user_passwd(passwd):
#     value = passwd
#     return value

# def get_user_nom(nom):
#     value = nom
#     return value

# def get_user_prenom(prenom):
#     value = prenom
#     return value


if __name__ == "__main__":
    # main = Main()
    # main.start()

    #     eel.init("web")
    eel.start("index.html", mode='mozilla', port=9998)
