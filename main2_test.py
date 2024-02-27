from chat import Chat
from chat import CRUD_Chat 
import eel
import time

chat = Chat()
db_msg = CRUD_Chat()
eel.init("web_chat")


# while True :
@eel.expose
def set_message(message:str) :
    db_msg.set_msg(1,message,1)
    time.sleep(60)
    print(db_msg.get_msg())


eel.start("index_chat.html", mode='mozilla')
        
    
