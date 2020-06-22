## importing socket module
from socket import gethostname, gethostbyname

## getting the hostname by socket.gethostname() method
hostname = gethostname()

## getting the IP address using socket.gethostbyname() method
ip_address = gethostbyname(hostname)

## printing the hostname and ip_address
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")