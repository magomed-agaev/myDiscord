from Connection import CRUD_authentification
from Chat import CRUD_Chat
from main import get_user_email

class Client:
    def __init__(self):
        self.connect = CRUD_authentification()
        self.chat = CRUD_Chat()
        self.email = get_user_email()

    
        # def get_email(self):
        #     print( self.email)

if __name__ == "__main__":
    client = Client()
    print(client.email)
    # client.get_email()