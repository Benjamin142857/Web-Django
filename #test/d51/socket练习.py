"""
    coding      : UTF-8
    Environment : Python 3.6
    Author      : Benjamin142857
    Data        : ---------
"""
import socket
import time
import re


class MySocket:
    def __init__(self, ip, host):
        self.sk = socket.socket()
        self.sk.bind((ip, host))
        self.sk.listen()
        self.get = ''
        self.url = '/'
        self.conn = None
        self.address = None

    def connection(self):
        self.conn, self.address = self.sk.accept()
        self.get = self.conn.recv(512).decode('utf-8')
        self.url = re.search('GET /.* HTTP/1.1', self.get).group().split(' ')[1]

        print('{} {}'.format(time.strftime('%Y-%m-%d %H:%M:%S'), self.url))

        if self.url == '/':
            self.response('socket.html', status=200)
        elif self.url == '/1.css':
            self.response('1.css', status=200)
        else:
            self.response('404.html', status=404)

        self.conn.close()

    def response(self, file_name, status):
        with open(file_name, 'r') as f:
            ret = f.read()
            f.close()

        self.conn.send(bytes('HTTP/1.1 {} ok\r\n\r\n{}'.format(str(status), ret), encoding='utf-8'))



if __name__ == '__main__':
    mysk = MySocket('127.0.0.1', 9000)

    while True:
        mysk.connection()

