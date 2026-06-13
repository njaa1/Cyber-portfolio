import socket

def scan_ports(host, start_port, end_port):
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"Port {port} is open")

if __name__ == "__main__":
    target = input("Enter host (ex: scanme.nmap.org): ")
    scan_ports(target, 20, 1024)
