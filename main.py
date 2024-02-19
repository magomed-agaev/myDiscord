from Connection import CRUD_authentification
from mysql.connector import Error
import eel

connect = CRUD_authentification()

def verification(email,passwd):
    for i in connect.read():
        print(i)

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
                print(i)
                print("connection ok")
            else :
                print("non")


# if __name__ == "__main__":
eel.init("web")
eel.start("index.html", mode='mozilla')