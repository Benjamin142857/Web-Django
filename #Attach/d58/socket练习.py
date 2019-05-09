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
        self.req_info = ''
        self.req_url = '/'
        self.url = []
        self.conn = None
        self.address = None


    def connection(self):
        self.conn, self.address = self.sk.accept()
        self.req_info = self.conn.recv(512).decode('utf-8')
        self.req_url = re.search('GET /.* HTTP/1.1', self.req_info).group().split(' ')[1]

        print('{} {}'.format(time.strftime('%Y-%m-%d %H:%M:%S'), self.req_url))

        for url in self.url:
            if self.req_url == url[0]:
                url[1](self.response)
                break
        else:
            self.response('404.html', status=404)

        self.conn.close()

    def response(self, file_name, status):
        with open(file_name, 'r') as f:
            ret = f.read()
            f.close()

        self.conn.send(bytes('HTTP/1.1 {} fuckyou\r\nserver: benjamin142857\r\nbefucker: alex\r\n\r\n{}'.format(str(status), ret), encoding='utf-8'))



if __name__ == '__main__':
    mysk = MySocket('127.0.0.1', 9000)

    def home(response):
        response('socket.html', status=200)

    def fun1(response):
        response('f1.html', status=200)

    mysk.url = [
        ('/', home),
        ('/fdf', fun1),
    ]
    while True:
        mysk.connection()

