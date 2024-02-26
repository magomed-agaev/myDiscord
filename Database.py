from dotenv import load_dotenv
import os 
import mysql.connector

#Chargement des données
load_dotenv(encoding="utf-8")  

class Database:
    def __init__(self):
        self.__host = os.getenv('host')
        self.__user = os.getenv('user')
        self.__password = os.getenv('passwd')
        self.__database = os.getenv('database')
         
    def __connect(self):    
        #connection base de donnée
        mydb = mysql.connector.connect(
        
            host = self.__host,
            user = self.__user,
            password = self.__password,
            database = self.__database,
            autocommit = True
        )   
        cursor = mydb.cursor()
        return mydb,cursor

    def query(self,req,value,modif=False):
        mydb, cursor = self.__connect()
        try:
            cursor.execute(req,value)
            if modif is False:
                result = cursor.fetchall()
                return result
        except:
            mydb.rollback()

        cursor.close()
        mydb.close()

        

if __name__ == "__main__":
    gestion = Database()
    