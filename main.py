import socket
import json
from _thread import *
from prometheus_client import Gauge, start_http_server

'''
create socket and returns the socket
'''


def server(port, IP):
    sock = socket.socket()
    sock.bind((IP, port))
    sock.listen()  # input = maximum clients
    return sock


'''
accept one client and make connection
'''


def accept(sock):
    connection, client_IP = sock.accept()
    # data_json = connection.recv(1024).decode()  # maximum byte
    # data = json.loads(data_json)
    return client_IP, connection


'''
get data from client and send to prometheus
'''


def get_data(conn, id):
    while True:
        data_json = conn.recv(1024).decode()  # maximum byte
        print(data_json)
        if not data_json:
            print("no more data")
            break
        data = json.loads(data_json)
        ram_percentage.labels(client_id=id).set(data['ram_percentage'])
        cpu_percentage.labels(client_id=id).set(data['cpu_percentage'])
        cpu_frequency.labels(client_id=id).set(data['cpu_frequency'])


ram_percentage = Gauge('ram_percentage', 'ram percentage per second', ['client_id'])
cpu_percentage = Gauge('cpu_percentage', 'cpu percentage per second', ['client_id'])
cpu_frequency = Gauge('cpu_frequency', 'cpu frequency per second', ['client_id'])

if __name__ == '__main__':
    start_http_server(1888)  # runs http server on prometheus
    serv = server(8080, '0.0.0.0')
    id = 100000
    while True:
        client_IP, connection = accept(serv)  # TCP
        print("connected to server")
        id -= 1
        start_new_thread(get_data, (connection, id))
