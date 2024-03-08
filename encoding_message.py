import base64
import emoji
import wave

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
    
    def encodage_all(self,msg:str=None,type=2,file_name:str=None):
        '''encodage encoding data utf-8 to bytes(not support emojis) 

        Arguments:
            msg -- string message-->type=1 or audio file-->type=2

        Returns:
            data in base64
        '''
        if type == 1: 
            data = msg.encode('utf-8')
            encoded_data = base64.b64encode(data)
            print('encodage ok')
            return encoded_data
        
        else :
            try:
                data = base64.b64encode(open(file_name, "rb").read())
                # encoded_data = base64.b64encode(data)
                print('encodage ok')
                return data
                
            except FileNotFoundError:
                print('Fichier introuvable.')
            except IOError:
                print('Erreur d\'ouverture.')
    
    def decodage_all(self,msg:str=None,type=2,file_name:str=None):
        '''decodage decoding data bytes to utf-8 (not support emojis) 

        Arguments:
            msg -- string message (base64)

        Returns:
            data text or audio wav in 'utf-8' 
        '''
        if type == 1:    
            decoded_data = base64.b64decode(msg)
            data = decoded_data.decode('utf-8')
            
            # return data
            return data
        else:
            decoded_data = base64.b64decode(msg)
            with wave.open(file_name,"wb") as wav_file:
                # 1 --> mono 2 -->stéréo
                wav_file.setnchannels(2)
                # 2 for 16 octet
                wav_file.setsampwidth(2)
                # frequence Hz
                wav_file.setframerate(44100)
                # write into wav
                wav_file.writeframes(decoded_data)
                
                

if __name__ == "__main__":
    cod = Data_codec()
    message = "I love pizza!❤️ " 
    message2 = "I love pizza! SSBsb3ZlIHBpenphIQ=="
    # message2 = '[(print)]'

    cod1 = cod.encodage_simple(message2)
    print(cod1)
    cod2 = cod.decodage_simple(cod1)
    print(cod2)
    
    
    # print(emojis)
    
    # print(emoji.demojize(message))

    # print(emoji.emojize(message))