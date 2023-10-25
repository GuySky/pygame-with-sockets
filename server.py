import socket, threading, json, pickle

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

SERVER_IP = socket.gethostbyname(socket.gethostname())                      #Server ip is here, it doesn't have to be your pc.
PORT = 55555                                                                #Connection key.
HEADER = 10000                                                              #Pre-info in messages.

#server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)               #May be needed. Try only if you know what you're doing.
server.bind((SERVER_IP, PORT))                                              #Server is alive now.
print(SERVER_IP)

clients_list = []


def run():
    while True:
        server.listen()                                                     #Listening to connections.
        client, addr = server.accept()                                      #If someine connected:~
        print(f'New client: {addr}')
        clients_list.append(client)
        start_listening(client, addr)                                       #New thread. Probably might be realized through multiproccessing.


def start_listening(client, addr):
    client_pr = threading.Thread(target=listening_pr, args=(client, addr,))
    client_pr.start()


def listening_pr(client, addr):

    while True:

        try:
            msg = client.recv(HEADER).decode().strip()                      #First get header.
            if msg:
                data = json.loads(msg)                                      #Message.
                broadcast(data, client, addr)                               #Translate to every client.

        except ConnectionResetError as _:                                   #Connection with current client lost.
            print(f'Client [{addr}] disconnected.')
            clients_list.remove(client)
            return


def broadcast(data, cl, addr):                                              #Translation to everyone.

    for client in clients_list:
        if client != cl:
            msg = json.dumps({str(addr): data})
            msg = f'{msg:<{HEADER}}'.encode()
            client.send(msg)


run()