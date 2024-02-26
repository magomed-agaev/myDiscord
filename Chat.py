from crud_chat import CRUD_Chat 
from client import Client

class Chat:
    def __init__(self):
        self.crud_chat = CRUD_Chat()
        self.client = Client()

    def print_msg(self):
        return self.crud_chat.get_msg()

    def print_time(self):
        return self.crud_chat.get_time()
    
    def print_sender(self):
        return  self.crud_chat.get_id_sender()
    