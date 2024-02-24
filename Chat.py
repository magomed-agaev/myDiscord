# from dotenv import load_dotenv
# import os 
from Database import Database
# from Connection import CRUD_authentification
from client import Client

# load_dotenv(encoding="utf-8")  

class CRUD_Chat():

    def __init__(self):
        self.dtb = Database()
   
    def set_msg(self, id_sender:int, message_is:str, id_type:int):
        '''create new row in table Chat_Public

        Arguments:
            id_sender -- id_user how send this message
            message_is -- message encoding in base64
            id_type -- messages types: -Txt:1 -Voice:2 -Video:3 -Picture:4
        '''
        req = "INSERT INTO Chat_public(id_sender,message_is,id_type) VALUES (%s,%s,%s,%s) "
        values = (id_sender, message_is, id_type)
        self.dtb.query(req,values)
        print("message add")
   

    def get_msg(self):
        '''read table chat_Public
        '''
        req = "SELECT id_sender,message_is,time FROM chat_public"
        return self.dtb.query(req)
        
        # for i in show_table:
        #     print (i)
             
    def delete_msg(self, id_sender:str):
        '''delete row in table chat_public 

        Arguments:
            id_sender -- id_user reference table users how send the message
        '''
        req = "DELETE FROM chat_Public WHERE id_sender = %s"
        value = id_sender
        self.dtb.query(req,value)

        print("message deleted successfully") 


if __name__ == "__main__":

    gestion = CRUD_Chat()
    client = Client()
    # print(gestion.set_msg(client._id,'hello',1))
    # gestion.delete("magomed.agaev@gmail.com")
    # gestion.read()
    # gestion.close_all()
        


        
      