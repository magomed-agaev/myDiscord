from Connection import CRUD_authentification
from mysql.connector import Error
import eel

connect = CRUD_authentification()

# def verification(email,passwd):
#     for i in connect.read():
#         re

eel.init("web")

eel.start("index.html", mode='mozilla',block=False)

@eel.expose
def Signup(nom:str, prenom:str, email:str, passwd:str):

    if "" not in [nom,prenom,email,passwd]:
        for i in connect.read():
            try :
                if i[3] != email:
                    connect.create(nom,prenom,email,passwd)

            except Error as e: 
                print ("Il semble y avoir une erreur veuillez réessayer")      

@eel.expose

def Signin(email:str, passwd:str):
    if "" not in [email,passwd]:
        for i in connect.read():
            if i[3] == email and i[4] == passwd:
               print("connection ok")
            #    return True
                
# @eel.expose
def get_user_email():
    email = eel.getUserEmail()()
    return email 



 
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



# if __name__ == "__main__":
