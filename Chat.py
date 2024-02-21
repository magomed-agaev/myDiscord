from dotenv import load_dotenv
# import os 
from Database import Database
from Connection import CRUD_authentification

load_dotenv(encoding="utf-8")  

class CRUD_Chat(Database):

    def __init__(self):
        super().__init__()

    def create(self,id_sender:int,message_is:str,id_type:int):
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
   

    def read(self):
        '''read table chat_Public
        '''

        req = "SELECT id,message_is,time FROM chat_public"
        return self.query(req)
        
        # for i in show_table:
        #     print (i)
    

    def update(self,colonne:str,new_name:str,user_id:int):
        '''update table users

        Arguments:
            colonne -- str name_column
            new_name -- str new information
            user_id -- INT id
        
        '''

        match(colonne):
            
            case 'nom':
                req = "UPDATE users SET nom = %s WHERE user_id = %s"
            case 'prenom':
                req = "UPDATE users SET prenom = %s WHERE user_id = %s"
            case 'email':
                req = "UPDATE users SET email = %s WHERE user_id = %s"
            case 'password_hash':
                req = "UPDATE users SET password_hash = %s WHERE user_id = %s"
            case _:
                print("Column name no found")
        
        values = (new_name,user_id)
        self.query(req,values,modif=True)

        print("users updated successfully")
          
    def delete(self,email:str):
        '''delete row in table users  

        Arguments:
            email -- email-inscription 
        '''
    
        req = "DELETE FROM users WHERE email = %s"
        value = email
        self.query(req,value)

        print("users deleted successfully")
    
    


if __name__ == "__main__":

    gestion = CRUD_Chat()
    # gestion.create("admin","admin","admin@admin2.com","admin")
    # gestion.update()
    # gestion.delete("magomed.agaev@gmail.com")
    # gestion.read()
    # gestion.close_all()
        


        
      