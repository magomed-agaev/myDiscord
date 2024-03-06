from authentification import Authentification
from database import Database
from chat import Chat
import eel
import webbrowser


chat = Chat()
login = Authentification()
dtb = Database()


eel.init("web")

@eel.expose
def Signup(nom:str, prenom:str, email:str, passwd:str):
    
    if "" not in [nom,prenom,email,passwd]:
        #Si l'email n'existe pas alors il crée l'utlisateur 
        if not login.read(email):
            try :
                login.set_new_user(nom,prenom,email,passwd)
                print("ok")
                # eel.redirect_chat()()
                webbrowser.open('http://localhost:9998/index_chat.html')
            except Exception as e: 
                print (f"Il semble y avoir une erreur veuillez réessayer, {e}")       

@eel.expose
def Signin(email:str,passwd:str):
    if "" not in [email,passwd]:
        for i in login.read(email):
            if i[3] == email and i[4] == passwd:
                global mail
                mail = email
                print("user connected !")              
                # eel.redirect_chat()()
                webbrowser.open('http://localhost:9998/index_chat.html')
                              
                                                     
# @eel.expose
# def get_message():
#     msg = eel.get_Message()()
#     print(msg)
#     return msg 

# eel.get_Message()(get_message)
# @eel.expose
# def get_user_email():
#     return eel.getUserEmail()()

# Permet de recuperer la variable global mail user 
def get_iduser():
    return login.get_Id_user(mail)
    
@eel.expose
def conversation(msg):
    print('ok')
    id_user = get_iduser()
    chat.set_msg(id_user,msg)
    
@eel.expose
def Affichage():
    return chat.get_msg_all()  

@eel.expose
def Time():
    return chat.get_time()

@eel.expose
def Author():
    return chat.get_sender_name()
       
@eel.expose
def close():
    dtb.close()

if __name__ == "__main__":
    
    eel.start("index.html", mode='mozilla',port=9998)
    # print(get_user_email())