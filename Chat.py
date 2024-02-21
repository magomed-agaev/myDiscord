from dotenv import load_dotenv
# import os 
from Database import Database
from Connection import CRUD_authentification
from client import Client

load_dotenv(encoding="utf-8")  

class CRUD_Chat(Database):

    def __init__(self):
        super().__init__()
        # super().__init__()
   
    def set_msg(self,id_sender:int,message_is:str,id_type:int):
        '''create new row in table Chat_Public

        Arguments:
            id_sender -- id_user how send this message
            message_is -- message encoding in base64
            id_type -- messages types: -Txt:1 -Voice:2 -Video:3 -Picture:4
        '''

        req = "INSERT INTO Chat_public(id_sender,message_is,id_type) VALUES (%s,%s,%s,%s) "
        values = (id_sender,message_is,id_type)
        self.query(req,values)
        print("message add")
   

    def get_msg(self):
        '''read table chat_Public
        '''

        req = "SELECT id_sender,message_is,time FROM chat_public"
        return self.query(req)
        
        # for i in show_table:
        #     print (i)
             
    def delete_msg(self,email:str):
        '''delete row in table users  

        Arguments:
            email -- email-inscription 
        '''
    
        req = "DELETE FROM chat_Public WHERE email = %s"
        value = email
        self.query(req,value)

        print("message deleted successfully")
    
    


if __name__ == "__main__":

    gestion = CRUD_Chat()
    # gestion.update()
    # gestion.delete("magomed.agaev@gmail.com")
    # gestion.read()
    # gestion.close_all()
        


        
      