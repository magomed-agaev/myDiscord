from authentification import Authentification
from mysql.connector import Error
from database import Database
from chat import Chat
import eel
# import time

chat = Chat()
login = Authentification()
dtb = Database()

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
                print (f"Il semble y avoir une erreur veuillez réessayer,{e}")       

@eel.expose
def Signin(email:str,passwd:str):
    if "" not in [email,passwd]:
        for i in login.read(email):
            if i[3] == email and i[4] == passwd:
                print("user exist")
                eel.redirect_chat()()
                                          
                
# @eel.expose
# def get_message():
#     msg = eel.get_Message()()
#     return msg 

@eel.expose
def conversation(message):
    id_sender = chat.get_id_sender()
    chat.set_msg(id_sender,message)

@eel.expose
def Affichage():
    return chat.get_msg()  

@eel.expose
def close():
    dtb.close()

if __name__ == "__main__":
    
    eel.start("index.html", mode='mozilla',port=9998)
    # print(get_user_email())