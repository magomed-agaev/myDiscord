# from dotenv import load_dotenv
# import os 
from authentification import CRUD_authentification
# from Chat import CRUD_Chat
# from main import *
# from main import Main       
from database import Database
# from Connection import CRUD_authentification


# load_dotenv(encoding="utf-8")  

class CRUD_Chat:

    def __init__(self):
        self.dtb = Database()
        self.connect = CRUD_authentification()
        # self._email = get_user_email()
        # self._id = self.connect.get_Id_user(self._email)
   
    def set_msg(self,id_sender,message_is, id_type=1):
        '''create new row in table Chat_Public

        Arguments:
            id_sender -- id_user how send this message
            message_is -- message encoding in base64
            id_type -- messages types: -txt:1 -sound:2 -video:3 -picture:4
        '''
        req = "INSERT INTO Chat_public(id_sender,message_is,id_type) VALUES (%s,%s,%s) "
        values = (id_sender, message_is, id_type)
        
        result = self.dtb.query(req,values)
        print(result)
        return result
        

    def get_id_sender(self):
        '''return id_sender in table chat_Public
        '''
        req = "SELECT id_sender FROM chat_public order by time limit 1  "
        id_sender = self.dtb.query(req,None)       
        #because id_sender is a tuple in a liste so [0][0] is for erase le liste and the tuple 
        return id_sender[0][0]
       
    def get_msg(self):
        '''return message in table chat_Public
        '''
        req = "SELECT message_is FROM chat_public"
        return self.dtb.query(req,None)
        
    def get_time(self):
        '''return time in table chat_Public
        '''
        req = "SELECT time FROM chat_public"
        return self.dtb.query(req,None)

    def get_sender_name(self,id_sender=1):
        req = "Select nom from users where user_id = %s"
        value = (id_sender)
        sender = self.dtb.query(req,value) 
        return sender    
             
    def delete_msg(self, id_sender:str):
        '''delete row in table chat_public 

        Arguments:
            id_sender -- reference table users how send the message
        '''
        req = "DELETE FROM chat_Public WHERE id_sender = %s"
        value = id_sender
        self.dtb.query(req,value)

        print("message deleted successfully") 


if __name__ == "__main__":

    gestion = CRUD_Chat()
    # gestion.set_msg(self,id_sender:int, message_is:str, id_type:int)
    # gestion.set_msg()
    # gestion.delete("magomed.agaev@gmail.com")
    # gestion.read()
    # gestion.close_all()
    print(gestion.get_sender_name())


        
      