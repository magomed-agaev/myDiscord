from authentification import Authentification
from mysql.connector import Error
from chat import Chat
import eel
import time

chat = Chat()
login = Authentification()


eel.init("web")

@eel.expose
def Signup(nom:str, prenom:str, email:str, passwd:str):
    
    if "" not in [nom,prenom,email,passwd]:
        if not login.read(email):
            try :
                
                login.set_new_user(nom,prenom,email,passwd)
                print("ok")
                eel.redirect_chat()()

            except Error as e: 
                print ("Il semble y avoir une erreur veuillez réessayer")      

@eel.expose
def Signin(email:str,passwd:str):
    if "" not in [email,passwd]:
        for i in login.read(email):
            if i[3] == email and i[4] == passwd:
                print("user exist")
                eel.redirect_chat()()
                                          
                
@eel.expose
def get_message():
    msg = eel.set_Message()()
    return msg 


@eel.expose
def set_message(message:str):
    id_sender = chat.get_sender()
    while True :
        chat.set_msg(id_sender,message)
        chat.get_msg()
        #wait 1s
        time.sleep(1)
        

if __name__ == "__main__":
    eel.start("index.html", mode='mozilla',port=9998)
    # print(get_user_email())