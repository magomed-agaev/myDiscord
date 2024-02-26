# from Database import Database
from crud_authentification import CRUD_authentification
# from Chat import CRUD_Chat
from main import get_user_email
# from main import Main

class Client:
    def __init__(self):
        self.connect = CRUD_authentification()
        self._email = get_user_email()
        self._id = self.connect.get_Id_user(self._email)
        

if __name__ == "__main__":
    client = Client
    