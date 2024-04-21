import socket

HOST = 'localhost'
PORT = 8099
# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = (HOST, PORT)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print('Server is listening on {}:{}'.format(*server_address))

while True:
    # Wait for a connection
    print('Waiting for a client to connect...')
    client_socket, client_address = server_socket.accept()
    print('Client connected from {}:{}'.format(*client_address))

    try:
        # Receive data from the client
        data = client_socket.recv(1024)
        print('Received data: {}'.format(data.decode()))

        # Send a response back to the client
        response = 'Hello from the server!'
        client_socket.sendall(response.encode())

    finally:
        # Clean up the connection
        client_socket.close()