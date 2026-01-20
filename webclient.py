import socket
import sys

if len(sys.argv) < 2:
    print("Usage: python webclient.py URL PORT")
    print("URL must be give, PORT is optional")
    sys.exit()

url = sys.argv[1]
port = int(sys.argv[2]) if len(sys.argv) > 2 else 80

with socket.socket() as s:
    s.connect((url, port))
    msg = f"GET / HTTP/1.1\r\nHost: {url}\r\nConnection: close\r\n\r\n".encode("ISO-8859-1")
    s.sendall(msg)
    d = s.recv(4096)
    print(d.decode("ISO-8859-1"))