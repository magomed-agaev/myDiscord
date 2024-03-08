import base64
import emoji

class Data_codec:
    def __init__(self):
        pass

    def encodage(self,msg:str):
        '''encodage encoding data utf-8 to bytes(support emojis) 

        Arguments:
            msg -- string message or audio file

        Returns:
            data in base64
        '''
        data_message = emoji.demojize(msg)
        # data = msg.encode('utf-8')
        data = data_message.encode('utf-8')
        encoded_data = base64.b64encode(data)
        return encoded_data

    def decodage(self,msg:str):
        '''decodage decoding data bytes to utf-8 (support emojis) 

        Arguments:
            msg -- string message (base64)

        Returns:
            data text or audio wav in 'utf-8' 
        '''
        decoded_data = base64.b64decode(msg)
        data = decoded_data.decode('utf-8')
        data_message = emoji.emojize(data)
        return data_message
    
    def encodage_simple(self,msg:str):
        '''encodage encoding data utf-8 to bytes(not support emojis) 

        Arguments:
            msg -- string message or audio file

        Returns:
            data in base64
        '''
        data = msg.encode('utf-8')
        encoded_data = base64.b64encode(data)
        return encoded_data
    
    def decodage_simple(self,msg):
        '''decodage decoding data bytes to utf-8 (not support emojis) 

        Arguments:
            msg -- string message (base64)

        Returns:
            data text or audio wav in 'utf-8' 
        '''
        decoded_data = base64.b64decode(msg)
        data = decoded_data.decode('utf-8')
        return data

if __name__ == "__main__":
    cod = Data_codec()
    message = "I love pizza!❤️ " 
    message2 = "I love pizza!"

    cod1 = cod.encodage_simple(message2)
    print(cod1)
    cod2 = cod.decodage_simple(cod1)
    print(cod2)
    
    # print(emojis)
    
    # print(emoji.demojize(message))

    # print(emoji.emojize(message))