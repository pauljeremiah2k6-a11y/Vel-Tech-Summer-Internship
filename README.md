# Vel-Tech-Summer-Internship
WEEK 1:

Project 1: Network Packet Sniffer using Python for basic network traffic monitoring and analysis.

Description

This project focuses on understanding how data moves across a network and how packets can be captured and analyzed using Python. It is designed as a beginner-level cybersecurity and networking project to explore packet sniffing concepts and basic traffic monitoring.

Features

- Built using Python programming
- Captures basic network packets
- Understands incoming and outgoing traffic flow
- Introduces cybersecurity monitoring concepts
- Works on Windows Command Prompt environment
- Helps visualize and analyze basic network activity (learning stage)

Outcome

- Gained hands-on experience in Python scripting
- Understood basics of networking and packet flow
- Learned how packet sniffing works in cybersecurity
- Improved understanding of system-level network monitoring tools
- Built foundation for advanced cybersecurity projects



WEEK 2:

Project 2: Network Packet Sniffer Using Python and Scapy

Description:
This project captures and analyzes network packets using Python and the Scapy library.

Tools Used:
- Python
- Scapy

Features:
- Captures live network packets
- Displays packet summaries
- Analyzes network protocols such as ARP and UDP

Outcome:
Successfully captured and monitored network traffic using Scapy.

Project 3: Python Port Scanner

Project Description
- This project is a simple port scanner built using Python.  
- It checks which ports are open or closed on a target IP address or website.

 Features
- Scan ports from 1 to 100 (or more)
- Detect open and closed ports
- Works on IP addresses and domain names
- Simple command-line interface

How It Works
- The tool uses Python's `socket` library to try connecting to ports.  
- If connection succeeds → port is OPEN  
- If it fails → port is CLOSED

Tools Used
- Python 3
- Socket module (built-in)

Week 3:

Project 4: Wireshark Traffic Analysis

Description
This project demonstrates network traffic analysis using Wireshark. DNS packets were captured and analyzed to understand how domain names are resolved into IP addresses.

Tools Used
- Wireshark
- Windows 11
- Wi-Fi Network

Features
- Packet Capture
- DNS Analysis
- Protocol Filtering
- Network Traffic Monitoring

Observations
- DNS queries and responses were captured.
- Domains such as c.pki.goog and ctldl.windowsupdate.com were observed.
- Network packets were analyzed to understand communication between the local machine and internet services.

Outcome
Successfully captured and analyzed network traffic using Wireshark and gained practical knowledge of DNS and packet analysis.

Project 5: Network Traffic Monitor Using Python

Project Description
This project is a simple Network Traffic Monitor developed using Python. It displays the active network connections on the computer, including local addresses, remote addresses, and connection status. The project helps users understand how their system communicates over a network.

Objective
To monitor and display the current network connections of a system and understand basic network traffic monitoring concepts.

Technologies Used
- Python 3
- psutil library

Features
- Displays active network connections.
- Shows local IP addresses and port numbers.
- Shows remote IP addresses and port numbers.
- Displays connection status such as:
  - ESTABLISHED
  - LISTEN
  - TIME_WAIT
  - NONE
- Easy to run and understand.

Project Structure

```
Network-Traffic-Monitor/
│
├── network_monitor.py
└── README.md
```

## ▶️ How to Run

### 1. Install the required library

```bash
pip install psutil
```

### 2. Run the program

```bash
python network_monitor.py
```

## 📋 Sample Output

```
Local Address : 192.168.100.77:64860
Remote Address: 14.167.152.255:39165
Status        : ESTABLISHED
----------------------------------------
Local Address : :::135
Remote Address: N/A
Status        : LISTEN
----------------------------------------
```

Explanation of Status

| Status | Meaning |
|----------|-----------|
| ESTABLISHED | Connection is currently active |
| LISTEN | Waiting for incoming connections |
| TIME_WAIT | Connection has recently closed |
| NONE | No specific TCP state (commonly UDP traffic) |
