import socket
import threading

port = 5050
formats = "utf-8"
buffer_for_length = 16
device_name = socket.gethostname()
ip_addr = socket.gethostbyname(device_name)
server_socket_addr = (ip_addr, port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_socket_addr)

server.listen()
print("Our server has started Listening...")

def handle_client(conn, adr):
    print("Connected to", adr)
    connected = True
    while connected:
        len_of_upcoming_msg = conn.recv(buffer_for_length).decode(formats)
        if len_of_upcoming_msg:
            len_of_upcoming_msg = int(len_of_upcoming_msg)
            msg = conn.recv(len_of_upcoming_msg).decode(formats)

            if msg == "OFF":
                print("Terminating connection with", adr)
                conn.send("Sent from Server: Goodbye! It was nice to serve you".encode(formats))
                connected = False
            else:
                print(msg)
                if int(msg) <= 40:
                    conn.send(f"Sent from Server: Salary TK{int(msg)*200}".encode(formats))
                elif int(msg) > 40:
                    conn.send(f"Sent from Server: Salary TK{8000+(int(msg)-40)*300}".encode(formats))
                else:
                    conn.send("Sent from Server: Enough Vowel I guess".encode(formats))
    conn.close()

while True:
    conns, adrs = server.accept()
    thread = threading.Thread(target=handle_client, args=(conns, adrs))
    thread.start()
