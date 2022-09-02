import socket
import time
import psutil
import json
'''
create socket and returns the socket
'''


def client(port, IP):
    sock = socket.socket()
    sock.connect((IP, port))  # input = maximum clients
    return sock


def send_data():
    dictionary_data = {}
    dictionary_data['cpu_percentage'] = psutil.cpu_percent(interval=1)
    dictionary_data['ram_percentage'] = psutil.virtual_memory().percent
    dictionary_data['cpu_frequency'] = psutil.cpu_freq()[0]
    return dictionary_data


def send_metrics(client_s):
    while True:
        data = send_data()
        data = json.dumps(data)
        print(data)
        client_s.send(data.encode())


if __name__ == '__main__':
    while True:
        #  if it didnt connect to the server, try to connect again
        try:
            clients = client(8080, '127.0.0.1')
            send_metrics(clients)
        except:
            print("retrying...")
            time.sleep(3)

