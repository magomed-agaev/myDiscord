# from Database import Database
from Connection import CRUD_authentification
# from Chat import CRUD_Chat
from main import *

class Client():
    def __init__(self):
        self.connect = CRUD_authentification()
        # self.chat = CRUD_Chat()
        self._email = get_user_email()
        self._id = self.connect.get_Id_user(self._email)
        # return user_id

if __name__ == "__main__":
    client = Client()
        # print(client._email)
    