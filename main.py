from authentification import CRUD_authentification
from mysql.connector import Error
from chat import CRUD_Chat
import eel


import time
# import eel


# chat = Chat()
db_msg = CRUD_Chat()

connect = CRUD_authentification()

eel.init("web")

@eel.expose
def Signup(nom:str, prenom:str, email:str, passwd:str):
    
    if "" not in [nom,prenom,email,passwd]:
        if not connect.read(email):
            try :
                
                connect.create(nom,prenom,email,passwd)
                print("ok")
                eel.redirect_chat()()

            except Error as e: 
                print ("Il semble y avoir une erreur veuillez réessayer")      

@eel.expose
def Signin(email:str,passwd:str):
    if "" not in [email,passwd]:
        for i in connect.read(email):
            if i[3] == email and i[4] == passwd:
                print("user exist")
                eel.redirect_chat()()
                                          
                
@eel.expose
def get_message():
    msg = eel.set_Message()()
    print(msg)


@eel.expose
def set_message(message:str):
    id_sender = db_msg.get_sender()
    print(id_sender)
    while True :
        db_msg.set_msg(id_sender,message)
        db_msg.get_msg()
        #wait 1s
        time.sleep(1)
        

if __name__ == "__main__":
    eel.start("index.html", mode='mozilla',port=9998)
    # print(get_user_email())