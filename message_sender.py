import socket

sender= socket.socket(family = socket.socket.AF_INET, type=socket.socket.SOCK_DGRAM)
sender.sendto(str.encode("Hello"), ('192.168.16.11', 7778))