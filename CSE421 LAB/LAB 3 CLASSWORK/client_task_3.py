import socket

port = 5050
formats = "utf-8"
buffer_for_length = 16
device_name = socket.gethostname()
ip_addr = socket.gethostbyname(device_name)
server_socket_addr = (ip_addr, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_socket_addr)

print("Our client is trying to connect..")


def message_to_send(msg):
    message = msg.encode(formats)
    message_length = len(message)  # send message size to server
    message_length = str(message_length).encode(formats)
    message_length += b" " * (buffer_for_length - len(message_length))

    client.send(message_length)
    client.send(message)

    sent_from_server = client.recv(2048).decode(formats)
    print(sent_from_server)


# while True:




message_to_send(f"aaaaaaaaa")

# message_to_send("OFF")
