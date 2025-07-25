# 🐚 Backdoor [Reverse Shell] - Master Remote Access Using Python Socket Tool

## 📖 Overview

This project demonstrates the creation of a **Reverse Shell Backdoor** using Python's `socket` module. A **reverse shell** allows an attacker (controller/master) to remotely execute shell commands on a compromised system (victim/client) after it initiates a connection to the attacker's machine.

⚠️ **Important: This project is for **educational** and **ethical hacking** purposes only.
⚠️ Legal Disclaimer: This code must **only** be used in environments where you have explicit permission. Unauthorized access or control over devices is **illegal and unethical**.

## 📂 Project Structure
This project consists of two parts: 
<br>
•	Server.py  <br>          # Server-side script for Listener/Controller running on Attacker machine.<br>
•	Client.py    <br>       #Client-side script for reverse Shell client to run on Victim machine.

##  `server.py` (Master Controller)

Server.py (Master Controller):<br>
This script runs on the attacker's machine and listens for incoming connections from the victim. Once connected, it sends shell commands and receives the output.<br>
It does the following:<br>
•	Listens for incoming connections on a specific IP and port.<br>
•	Accepts a connection from the client (victim).<br>
•	Sends commands to the victim.<br>
•	Receives and displays the output of the commands sent.<br>


##	Explanation:<br>
•	Binds to port 4444 and waits for incoming connections.<br>
•	Once connected, takes input from the attacker and sends it to the client.<br>
•	Receives and prints the output from the client<br>


## Client.py (Victim shell):<br>
This script runs on the target/victim machine and is responsible for:<br>
•	Initiating a connection to the attacker’s (server) machine.<br>
•	Receiving commands from the attacker.<br>
•	Executing those commands using the system shell.<br>
•	Sending back the output to the attacker.<br>
<br>

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
This project demonstrates the fundamentals of socket-based remote access tools by implementing a basic reverse shell using Python. It showcases how a client (victim) machine can be controlled remotely through a persistent connection initiated by the client itself. The attacker (server) can send shell commands, navigate the victim's file system, and receive command output in real-time.<br>
The simplicity of the implementation provides a hands-on understanding of:<br>
•	How TCP sockets can be used to establish bidirectional communication.<br>
•	The role of reverse shells in remote access tools.<br>
•	How basic command execution and file system interaction is done remotely.<br>
While this tool is for educational and ethical use only, it lays a strong foundation for understanding how backdoors work in penetration testing, red teaming, and ethical hacking. You can extend this project further by adding encryption, authentication, file transfer, or a multi-client architecture. <br>


**Author:** *Arnab Kumar Hembram*  
**Date:** *25-07-2025*
