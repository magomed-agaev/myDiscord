from database import Database
from authentification import Authentification
from datetime import datetime

class Chat:
    def __init__(self):
        self.dtb = Database()
        self.connect = Authentification()
        
    def set_msg(self,id_sender,message_is, id_type=1):
        '''
        create new row in table Chat_Public
        Arguments:
            id_sender -- id_user how send this message
            message_is -- message encoding in base64
            id_type -- messages types: -txt:1 -sound:2 -video:3 -picture:4
        '''
        req = "INSERT INTO Chat_public(id_sender,message_is,id_type) VALUES (%s,%s,%s) "
        values = (id_sender, message_is, id_type)
        self.dtb.query(req,values)
    
    def get_id_sender(self):
        '''
        return id_sender
        '''
        req = "SELECT id_sender FROM chat_public order by time limit 1"
        id_sender = self.dtb.query(req,None) 
        # return id_sender      
        # Because id_sender is a tuple in a liste so [0][0] is for erase le liste and the tuple 
        return id_sender[0][0]

    # def get_msg_all(self):
    #     '''
    #     return message
    #     '''
    #     req = "select prenom,message_is,id_type,time from users inner join chat_public ON users.user_id = chat_public.id_sender order by id ;"
    #     result = self.dtb.query(req,None)
    #     return result

    def get_msg_all(self):
        '''
        return message
        '''
        req = "SELECT prenom, message_is, id_type, DATE_FORMAT(time, '%d/%m/%Y %H:%i:%s') AS time_formatée FROM users \
                INNER JOIN chat_public ON users.user_id = chat_public.id_sender order by id;"

        result = self.dtb.query(req,None)
        # tab = []
        # compt = len(result)
        # for i in range(0,compt):
        #     return i
            # result[i]
        # return result[1] 
        return result


    def get_msg(self):
        '''
        return message
        '''
        req = "SELECT message_is FROM chat_public"
        result = self.dtb.query(req,None)
        tab = []
        for i in result : 
           # for i in range (len(result)-1):
           tab.append(i[0])
        return tab

    # def get_time(self):
    #     '''return message time
    #     '''
    #     req = "SELECT time FROM chat_public"
    #     result = self.dtb.query(req,None)
    #     tab = []
    #     for i in result : 
    #        # for i in range (len(result)-1):
    #     #    valeur = i[0]
    #        tab.append(i[0].strftime('%d/%m/%Y %H:%M'))
    #     return tab
    def get_time(self):
        '''return message time
        '''
        req = " SELECT DATE_FORMAT(time, '%d/%m/%Y %H:%i:%s') AS date_formatée FROM chat_public;"
        result = self.dtb.query(req,None)
        tab = []
        for i in result : 
        
            tab.append(i[0])
        return tab

    def get_sender_name(self):
        '''
        return sender name 
        '''
        req = "select nom from chat_public inner join users ON chat_public.id_sender = users.user_id;"
        
        # value = (self.get_id_sender(),)
        sender = self.dtb.query(req,None) 
        # return sender
        tab = []
        for i in sender : 
           # for i in range (len(result)-1):
           tab.append(i[0])
        return tab   
             
    def delete_msg(self, id_sender:int):
        req = "DELETE FROM chat_Public WHERE id_sender = %s"
        value = (id_sender,)
        self.dtb.query(req,value)
        print("message deleted successfully") 


if __name__ == "__main__":

    gestion = Chat()

    # gestion.set_msg(self,id_sender:int, message_is:str, id_type:int)
    # gestion.set_msg(1,'wsh_test_1')
    # gestion.delete("magomed.agaev@gmail.com")
    # gestion.delete_msg(9)
    # gestion.read()
    # gestion.close_all()
    # print(gestion.get_sender_name())
    # print(gestion.get_id_sender())
    # print(gestion.get_time())
    print(gestion.get_msg_all())




        
      
    
