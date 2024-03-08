from authentification import Authentification
from encoding_message import Data_codec
from database import Database
from chat import Chat
from audio import Audio
from hashage import hashage
import eel
import webbrowser
import os

audio = Audio()
chat = Chat()
login = Authentification()
dtb = Database()
codec = Data_codec()

eel.init("web")


@eel.expose
def Signup(nom: str, prenom: str, email: str, passwd: str):

    if "" not in [nom, prenom, email, passwd]:
        # Si l'email n'existe pas alors il crée l'utlisateur
        if not login.read(email):
            # hashage password
            password_hash = hashage(passwd)
            try:
                login.set_new_user(nom, prenom, email, password_hash)
                print("ok")
                global mail
                mail = email
                # eel.redirect_chat()()
                webbrowser.open('http://localhost:9998/index_chat.html')
            except Exception as e:
                print(f"Il semble y avoir une erreur veuillez réessayer, {e}")


@eel.expose
def Signin(email: str, passwd: str):
    if "" not in [email, passwd]:
        for i in login.read(email):
            # hashage password
            password_hash = hashage(passwd)
            if i[3] == email and i[4] == password_hash:
                global mail
                mail = email
                print("user connected !")
                # eel.redirect_chat()()
                webbrowser.open('http://localhost:9998/index_chat.html')


# @eel.expose
# def get_message():
#     msg = eel.get_Message()()
#     print(msg)
#     return msg


# @eel.expose
# def get_user_email():
#     return eel.getUserEmail()()

# Permet de recuperer la variable global mail user
def get_iduser():
    '''get_iduser is fonction how get email from Signin

    Returns:
        _description_
    '''
    return login.get_Id_user(mail)


@eel.expose
def conversation(msg: str, id_type=1):
    '''conversation save message into the database with CRUD chat

    Arguments:
        msg -- message str from js
    '''
    id_user = get_iduser()
    chat.set_msg(id_user, msg, id_type)

# @eel.expose
# def decode_simple(msg:str):
#     print(codec.decodage_simple(msg))
#     return codec.decodage_simple(msg)


@eel.expose
def Affichage():
    '''Affichage in a expose fonction for eel

    Returns:
        all the lines with messages decoding from chat_public table
    '''
    msg_all = chat.get_msg_all()
    # Create a new list by copying each tuple from the msg_all list while modifying the message decoding
    decode_all_msg = [(element[0], element[1], codec.decodage_all(
        element[2], element[3], 'test.wav'), element[3], element[4]) for element in msg_all]
    if os.path.exists('test.wav'):
        os.remove('test.wav')
    return decode_all_msg


@eel.expose
def set_audio():
    file_name = audio.generator_file_name()
    audio.record(file_name)
    encoding_wav = codec.encodage_all(None, 2, file_name)
    id_user = get_iduser()
    chat.set_msg(id_user, encoding_wav, 2, file_name)
    os.remove(file_name)


@eel.expose
def get_audio(id):

    file_name = audio.generator_file_name()
    audio_encoding = chat.get_msg(id)
    codec.decodage_all(audio_encoding, 2, file_name)
    audio.play(file_name)
    os.remove(file_name)


@eel.expose
def Time():
    return chat.get_time()


@eel.expose
def Author():
    return chat.get_sender_name()


@eel.expose
def close():
    dtb.close()


if __name__ == "__main__":
    # gets the index.html file in mozilla
    eel.start("index.html", mode='mozilla', port=9998)
