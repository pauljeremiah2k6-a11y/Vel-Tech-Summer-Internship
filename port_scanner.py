import socket

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # 1 second timeout

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
        else:
            print(f"[CLOSED] Port {port}")

        sock.close()

    except socket.gaierror:
        print("Hostname could not be resolved")
    except socket.error:
        print("Could not connect to server")


target = input("Enter target IP or website (example: 127.0.0.1): ")

print("\nScanning ports 1 to 100...\n")

for port in range(1, 101):
    scan_port(target, port)