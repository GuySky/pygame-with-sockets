import socket, threading, json

class Network:

    def __init__(self):
        self.SERVER_IP = socket.gethostbyname(socket.gethostname())
        self.PORT = 55555
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.SERVER_IP, self.PORT))
        self.HEADER = 10000
        self.data = {self.sock: {'x': 0, 'y': 0, 'width': 0, 'height': 0, 'type': 'nothing'}}
        #self.sock.setblocking(0)
        thread_receive = threading.Thread(target=self.receiving_thread)
        thread_receive.start()
    
    def sending_thread(self, data):
        try:
            msg = json.dumps(data)
            msg = f'{msg:<{self.HEADER}}'.encode()
            self.sock.send(msg)
        except:
            print('Ошибка 1')
            msg = json.dumps(self.data)
            msg = f'{msg:<{self.HEADER}}'.encode()
            self.sock.send(msg)
            return
    
    def receiving_thread(self):
        while True:
            try:
                msg = self.sock.recv(self.HEADER).decode().strip()
                if msg:
                    self.data = json.loads(msg)
                    print(self.data)
            except:
                print('Ошибка 2')
                msg = json.dumps(self.data)
                msg = f'{msg:<{self.HEADER}}'.encode()
                self.sock.send(msg)
                return
    
    def get_data(self):
        return self.data
    
    def close_connection(self):
        self.sock.close()


if __name__ == '__main__':
    n = Network()
    while True:
        n.sending_thread({'x': 0, 'y': 0})
