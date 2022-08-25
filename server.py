import threading
import socket
from typing import Tuple

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(('0.0.0.0', 55555))

clients = []
def checkConn():
    while True:
        data, address = sock.recvfrom(1028)
        if address not in clients:
            sock.sendto(address[0].encode('ascii'), address)
            sock.sendto(str(address[1]).encode('ascii'), address)
            clients.append(address)
        returnVal = data.decode('ascii')
        for i in clients:
            if i != address:
                sock.sendto(returnVal.encode('ascii'), i)
        checkConn()

connCheck = threading.Thread(target=checkConn, args=())
connCheck.start()