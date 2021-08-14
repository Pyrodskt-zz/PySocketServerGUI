import socket
import os



def run_client(po, ip_addr, file, pbar):
    SEPARATOR = "<SEPARATOR>"
    BUFFER_SIZE = 1024

    host = ip_addr

    port = po
    prog = 0
    s = socket.socket()
    print(f'connecting to {host}:{port}')

    s.connect((host, port))
    filesize = os.path.getsize(file)
    print("connected")
    s.send(f"{file}{SEPARATOR}{filesize}".encode())
    with open(file, "rb") as f:
        while True:

            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break

            s.sendall(bytes_read)
            prog += len(bytes_read)/int(filesize) * 100
            pbar.Update(prog)

    print("sent")
    s.close()

