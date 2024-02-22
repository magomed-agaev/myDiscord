import socket
import threading
import eel
# Function to handle client connections

eel.init('web')


def handle_client(client_socket, client_address):
    print(f"Connection from {client_address}")

    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break

        print(f"Received message from {client_address}: {data}")

        # Echo the received message back to the client
        client_socket.sendall(data.encode('utf-8'))

    print(f"Client {client_address} disconnected")
    client_socket.close()


# Set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(5)

print("Server listening on port 8080...")

# Main server loop
while True:
    # Accept incoming connections
    client_socket, client_address = server_socket.accept()

    # Start a new thread to handle the client
    client_thread = threading.Thread(
        target=handle_client, args=(client_socket, client_address))
    client_thread.start()
