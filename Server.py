import socket
import os


def run_server(port, pbar):
    SERVER_HOST = "0.0.0.0"
    SERVER_PORT = port
    prog = 0
    BUFFER_SIZE = 1024
    SEPARATOR = "<SEPARATOR>"

    s = socket.socket()

    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(5)

    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
    client_socket, address = s.accept()

    print(f"[+] {address} is connected")

    received = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)

    filename = os.path.basename(filename)
    filesize = int(filesize)

    with open(filename, "wb") as f:
        while True:
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                break

            f.write(bytes_read)
            prog += len(bytes_read) / int(filesize) * 100
            pbar.update(prog)
    print("sent")
    client_socket.close()