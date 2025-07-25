# 🐚 Backdoor [Reverse Shell] - Master Remote Access Using Python Socket Tool

## 📖 Overview

This project demonstrates the creation of a **Reverse Shell Backdoor** using Python's `socket` module. A **reverse shell** allows an attacker (controller/master) to remotely execute shell commands on a compromised system (victim/client) after it initiates a connection to the attacker's machine.

⚠️ **Important: This project is for **educational** and **ethical hacking** purposes only.
⚠️ Legal Disclaimer: This code must **only** be used in environments where you have explicit permission. Unauthorized access or control over devices is **illegal and unethical**.

## 📂 Project Structure
This project consists of two parts:
•	Server.py           # Server-side script for Listener/Controller running on Attacker machine.
•	Client.py           #Client-side script for reverse Shell client to run on Victim machine.

##  `server.py` (Master Controller)

Server.py (Master Controller):
This script runs on the attacker's machine and listens for incoming connections from the victim. Once connected, it sends shell commands and receives the output.
It does the following:
•	Listens for incoming connections on a specific IP and port.
•	Accepts a connection from the client (victim).
•	Sends commands to the victim.
•	Receives and displays the output of the commands sent.


##	Explanation:
•	Binds to port 4444 and waits for incoming connections.
•	Once connected, takes input from the attacker and sends it to the client.
•	Receives and prints the output from the client


## Client.py (Victim shell):
This script runs on the target/victim machine and is responsible for:
•	Initiating a connection to the attacker’s (server) machine.
•	Receiving commands from the attacker.
•	Executing those commands using the system shell.
•	Sending back the output to the attacker.


## How to Use

### ✅ On Attacker (Master) Machine:
```bash
python server.py
```

### ✅ On Victim Machine:
1. Replace `YOUR_SERVER_IP` in `client.py` with your attacker's IP.
2. Run the client:
```
python client.py
```


## 🧪 Ethical Testing Platforms

- [TryHackMe](https://tryhackme.com/)
- [Hack The Box](https://www.hackthebox.com/)
- [OverTheWire](https://overthewire.org/)

## 📜 License

This project is licensed for educational use. Do **not** use this on devices or networks you do not own or have permission to test.

## Conclusion:
This project demonstrates the fundamentals of socket-based remote access tools by implementing a basic reverse shell using Python. It showcases how a client (victim) machine can be controlled remotely through a persistent connection initiated by the client itself. The attacker (server) can send shell commands, navigate the victim's file system, and receive command output in real-time.
The simplicity of the implementation provides a hands-on understanding of:
•	How TCP sockets can be used to establish bidirectional communication.
•	The role of reverse shells in remote access tools.
•	How basic command execution and file system interaction is done remotely.
While this tool is for educational and ethical use only, it lays a strong foundation for understanding how backdoors work in penetration testing, red teaming, and ethical hacking. You can extend this project further by adding encryption, authentication, file transfer, or a multi-client architecture. 


**Author:** *Arnab Kumar Hembram*  
**Date:** *25-07-2025*
