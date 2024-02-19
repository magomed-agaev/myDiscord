from dotenv import load_dotenv
import os 
import mysql.connector

class Database:

    def __init__(self):
        #Chargement des données
        load_dotenv(encoding="utf-8")
        
        #connection base de donnée
        self.mydb = mysql.connector.connect(
        
            host = os.getenv('host'),
            user = os.getenv('user'),
            password = os.getenv('passwd'),
            database = os.getenv('database'),
            autocommit = True
        )

        self.cursor = self.mydb.cursor()
        
    def create(self,last_name:str,name:str,email:str,passwd_hash:str):
        '''create new row in database

        Arguments:
            last_name -- str
            name -- str
            email -- str
            passwd_hash -- str  
        '''
        try:
            sql = "INSERT INTO users(nom,prenom,email,password_hash) VALUES (%s,%s,%s,%s) "
            values = (last_name,name,email,passwd_hash)
            
            self.cursor.execute(sql,values)
            print("users Added successfully !")

                    
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            self.mydb.rollback()

    def read(self):
        '''read table users database
        '''
        try:
            sql = "SELECT * FROM users"
            self.cursor.execute(sql)
            show_table = self.cursor.fetchall()
            return show_table
            # for i in show_table:
            #     print (i)

                    
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            self.mydb.rollback()
 
        
    def update(self,colonne:str,new_name:str,user_id:int):
        '''update table users

        Arguments:
            colonne -- str name_column
            new_name -- str new information
            user_id -- INT id
        
        '''
        
        try:
            match(colonne):
                
                case 'nom':
                    sql = "UPDATE users SET nom = %s WHERE user_id = %s"
                case 'prenom':
                    sql = "UPDATE users SET prenom = %s WHERE user_id = %s"
                case 'email':
                    sql = "UPDATE users SET email = %s WHERE user_id = %s"
                case 'password_hash':
                    sql = "UPDATE users SET password_hash = %s WHERE user_id = %s"
                case _:
                    print("Column name no found")
            
            values = (new_name,user_id)
            self.cursor.execute(sql,values)

            print("users updated successfully")
              
        
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            self.mydb.rollback()
    
    
    def delete(self,email:str):
        '''delete row in table users  

        Arguments:
            email -- email-inscription 
        '''
        try:    
            sql = "DELETE FROM users WHERE email = %s"
            self.cursor.execute(sql,(email,))

            print("users deleted successfully")
        
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            self.mydb.rollback()

    def close_all(self):
        self.cursor.close()
        self.mydb.close()


if __name__ == "__main__":

    database_ = Database()
    # database_.create("admin","admin","admin@admin1.com","admin")
    # database_.update()
    database_.delete("")
    print(database_.read())


    # database_.close_all()
        