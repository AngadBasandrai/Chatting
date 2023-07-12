import threading
import socket
import playsound

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.connect(('192.168.1.14', 55555))

name = input("Type your name-> ")
sock.send(' '.encode('ascii'))
data = sock.recvfrom(1028)
data2 = sock.recvfrom(1028)
ip = (data[0].decode('ascii'), data2[0].decode('ascii'))
sock.send(f"{name} just entered the party!".encode('ascii'))

def checkConn():
    while True:
        data = sock.recvfrom(1028)
        playsound.playsound("squeak.wav")
        print()
        print(data[0].decode('ascii'))            
        checkConn()

def getInput():
    while True:
        v = input()
        sock.send((name + ',(' + ip[0] + ', ' + ip[1] + ")" + ">>" + v).encode())
        getInput()

connCheck = threading.Thread(target=checkConn, args=())
connCheck.start()

inp = threading.Thread(target=getInput, args=())
inp.start()