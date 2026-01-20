import socket
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 28333
msg = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 6\r\nConnection: close\r\nHello!\r\n\r\n"

with socket.socket() as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', PORT))
    s.listen()

    while True:
        new_conn = s.accept()
        new_socket = new_conn[0]
        
        while True:
            d = new_socket.recv(4096)
            sender = new_socket.getpeername()
            print("Received from:", sender[0], "port:", sender[1])
            if "\r\n\r\n" in d.decode("ISO-8859-1"):
                break

        new_socket.sendall(msg.encode("ISO-8859-1"))
        new_socket.close()
