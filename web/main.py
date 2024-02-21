import socket
import threading
import eel
# Function to handle client connections

eel.init('web')

eel.start('index.html', mode='Mozilla')

