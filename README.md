# 🐚 Backdoor [Reverse Shell] - Master Remote Access Using Python Socket Tool

## 📖 Overview

This project demonstrates the creation of a **Reverse Shell Backdoor** using Python's `socket` module. A **reverse shell** allows an attacker (controller/master) to remotely execute shell commands on a compromised system (victim/client) after it initiates a connection to the attacker's machine.

⚠️ **Important: This project is for **educational** and **ethical hacking** purposes only.
⚠️ Legal Disclaimer: This code must **only** be used in environments where you have explicit permission. Unauthorized access or control over devices is **illegal and unethical**.

## 📂 Project Structure

reverse_shell/
├── server.py      # Server-side script for Listener/Controller running on Attacker machine.
└── client.py      # Client-side script for reverse Shell client to run on Victim machine.


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


## `client.py` (Reverse Shell)

This script runs on the **victim's machine** and connects back to the attacker.

### 🔹 Code Overview

- Connects to the attacker's IP and port `4444`.
- Receives and executes shell commands.
- Sends command output back to the attacker.
- Handles directory navigation (e.g., `cd ..`).

---

## 🛠 How to Use

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


```

## 🧪 Ethical Testing Platforms

- [TryHackMe](https://tryhackme.com/)
- [Hack The Box](https://www.hackthebox.com/)
- [OverTheWire](https://overthewire.org/)

---

## 📜 License

This project is licensed for educational use. Do **not** use this on devices or networks you do not own or have permission to test.

---

**Author:** *Arnab Kumar Hembram*  
**Date:** *25-07-2025*
