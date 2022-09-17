# Import the library
import serial
from socket import*
serv_addr='192.168.161.129'
serv_port=7000
client_sock=socket(AF_INET,SOCK_DGRAM)

try:
    fabkit = serial.Serial('COM3', 9600)
except:
    print("Failed to connect")
    exit()

while 1: #read
    line = fabkit.readline()
    print(line)
    msg = str(line)
    client_sock.sendto(msg.encode(), (serv_addr, serv_port))
    mod_msg, s = client_sock.recvfrom(2048)
    print("From Server:", mod_msg.decode())

# We should close the connection... but since there's a while 1 loop before, we never reach this
fabkit.close()
