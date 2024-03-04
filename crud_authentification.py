# import mysql.connector
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="magaev",
#     database="my_discord"
# )

# cursor = mydb.cursor()

# nom = ""
# prenom = ""
# email = ""
# password = ""

# insert_query = "INSERT INTO users (nom, prenom, email, password) VALUES (%s,%s,%s,%s)"
# user_data = (nom, prenom, email, password)
# cursor.execute(insert_query, user_data)

# mydb.commit()


# cursor.close()
# mydb.close()
# import eel


# class DatabaseConnection:
#     def __init__(self):
#         self.host = "localhost"  # default localhost
#         self.db = "my_discord"  # name of the database
#         self.user = "root"  # default root
#         self.passwd = "magaev"  # default password
#         self.my_discord = None

#     def connect(self):
#         import mysql.connector
#         self.my_discord = mysql.connector.connect(
#             host=self.host, user=self.user, password=self.passwd, database=self.db
#         )
#         if self.my_discord.is_connected():
#             print("Connection successful")
#         else:
#             print("Error connecting to the database")

#     @eel.expose
#     def signup(self):
#         first_name = input("Enter firstname: ")
#         last_name = input("Enter lastname: ")
#         email = input("Enter email: ")
#         password = input("Enter password: ")

#         print(f"User: {first_name, last_name}")
#         print(f"Password: {password}")
#         print(f"Email: {email}")

#         cursor = self.my_discord.cursor()
#         sql = "INSERT INTO users (nom, prenom, email, password_hash) VALUES (%s, %s,%s, %s)"
#         values = (first_name, last_name, email, password)
#         try:
#             cursor.execute(sql, values)
#             self.my_discord.commit()
#             print("Insertion successful")
#         except Exception as e:
#             print(f"Error inserting data: {e}")
#             self.my_discord.rollback()
#         finally:
#             cursor.close()
#             self.my_discord.close()


# # Usage example:
# db_connection = DatabaseConnection()
# db_connection.connect()
# db_connection.signup()
# import eel
from Database import Database


class CRUD_authentification():

    def __init__(self):
        self.dtb = Database()

    def create(self, nom: str, prenom: str, email: str, password_hash: str):
        '''create new row in database

        Arguments:
            last_name -- str
            name -- str
            email -- str
            passwd_hash -- str  
        '''

        req = "INSERT INTO users(nom,prenom,email,password_hash) VALUES (%s,%s,%s,%s) "
        values = (nom, prenom, email, password_hash)
        self.dtb.query(req, values)

    def read(self, email: str):
        '''read user row in tables users

        Returns:
            With email get all information user 
        '''

        req = "SELECT * FROM users where email = %s"
        value = (email,)
        return self.dtb.query(req, value)

    def update(self, colonne: str, new_name: str, user_id: int):
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

        values = (new_name, user_id)
        self.dtb.query(req, values, modif=True)

        print("users updated successfully")

    def delete(self, email: str):
        '''delete row in table users  

        Arguments:
            email -- email-inscription 
        '''

        req = "DELETE FROM users WHERE email = %s"

        value = (email,)
        self.dtb.query(req, value)

        print("users deleted successfully")

    # @eel.expose
    def get_Id_user(self, email: str):
        '''get user user_id how send the message 

        Arguments:
            email -- str

        Returns:
            User_id
        '''
        req = "SELECT user_id FROM users where email = %s"
        value = (email,)

        return self.dtb.query(req, value)


if __name__ == "__main__":

    gestion = CRUD_authentification()
    # gestion.create("admin","admin","admin@admin2.com","admin")
    # gestion.update()
    # gestion.delete("magomed.agaev@gmail.com")
    print(gestion.read('admin@admin1.com'))
    # gestion.close_all()
    # gestion.get_Id_user('admin@admin1.com')
