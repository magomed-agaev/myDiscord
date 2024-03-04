import base64


def encodage(msg):
    encoded_msg = base64.b64encode(msg.encode())
    print(encoded_msg.decode())
    return encoded_msg


encodage("wsh")
