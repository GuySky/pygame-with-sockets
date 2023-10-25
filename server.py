import socket, threading, json, pickle

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

SERVER_IP = socket.gethostbyname(socket.gethostname())
PORT = 55555
HEADER = 10000

#server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((SERVER_IP, PORT))
print(SERVER_IP)

clients_list = []

def run():
    while True:
        server.listen()
        client, addr = server.accept()
        print(f'Подключен клиент: {addr}')
        clients_list.append(client)
        start_listening(client, addr)

def start_listening(client, addr):
    client_pr = threading.Thread(target=listening_pr, args=(client, addr,))
    client_pr.start()

def listening_pr(client, addr):
    while True:
        try:
            msg = client.recv(HEADER).decode().strip()
            if msg:
                data = json.loads(msg)
                #print(str(client) + ': ' + str(data))
                broadcast(data, client, addr)
        except ConnectionResetError as _:
            print('Клиент отключился.')
            clients_list.remove(client)
            return
        
def broadcast(data, cl, addr):
    for client in clients_list:
        #try:
        if client != cl:
            msg = json.dumps({str(addr): data})
            msg = f'{msg:<{HEADER}}'.encode()
            client.send(msg)
            #print(cl)
            #print(client)
        #except:
        #    print('Ошибка 1')

run()