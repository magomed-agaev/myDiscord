from crud_authentification import CRUD_authentification
from mysql.connector import Error
import eel

connect = CRUD_authentification()

eel.init("web","web_chat")

@eel.expose
def Signup(nom:str, prenom:str, email:str, passwd:str):
    
    if "" not in [nom,prenom,email,passwd]:
        
        for i in connect.read(email):
            try :
                if i[3] != email:
                    connect.create(nom,prenom,email,passwd)
                    print("ok")
                    return True
            except Error as e: 
                print ("Il semble y avoir une erreur veuillez réessayer")      

@eel.expose
def Signin(email:str,passwd:str):
    print(passwd)
    if "" not in [email,passwd]:
        for i in connect.read(email):
            if i[3] == email and i[4] == passwd:
                print("connection ok")
                return True
                
@eel.expose
def get_user_email():
    email = eel.getUserEmail()()
    return email


if __name__ == "__main__":
    eel.start("index.html", mode='mozilla',port=9998)
    