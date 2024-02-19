from dotenv import load_dotenv
import os 
from Database import Database
from mysql.connector import Error

load_dotenv(encoding="utf-8")  

class CRUD_authentification(Database):

    def __init__(self):
        super().__init__()

    def create(self,last_name:str,name:str,email:str,passwd_hash:str):
        '''create new row in database

        Arguments:
            last_name -- str
            name -- str
            email -- str
            passwd_hash -- str  
        '''

        req = "INSERT INTO users(nom,prenom,email,password_hash) VALUES (%s,%s,%s,%s) "
        values = (last_name,name,email,passwd_hash)
        
        self.query(req,values)
        print("users Added successfully !")

        

    def read(self):
        '''read table users database
        '''

        req = "SELECT * FROM users"
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

    gestion = CRUD_authentification()
    # gestion.create("admin","admin","admin@admin2.com","admin")
    # gestion.update()
    # gestion.delete("magomed.agaev@gmail.com")
    print(gestion.read())
    # gestion.close_all()
        


        
                    
 
        