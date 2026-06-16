import psutil

print("=== Network Traffic Monitor ===\n")

connections = psutil.net_connections()

for conn in connections:
    try:
        local = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
        remote = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"

        print(f"Local Address : {local}")
        print(f"Remote Address: {remote}")
        print(f"Status        : {conn.status}")
        print("-" * 40)

    except Exception:
        pass