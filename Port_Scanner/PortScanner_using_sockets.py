# using sockets
import socket
import re

ip_pattern = re.compile(r"^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})(\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})){3}$")
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

port_minimum = 0
port_maximum = 65535

open_port = []

while True:
    ip_add_entered = input('\nEnter the IP address for scanning:  ')
    if ip_pattern.search(ip_add_entered):
        print(f"{ip_add_entered} is a valid IP address.")
        break

while True:
    print("RANGE OF PORTS")
    port_range = input("Enter a port range(e.g. start-end):  ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))
    if port_range_valid:
        port_minimum = int(port_range_valid.group(1))
        port_maximum = int(port_range_valid.group(2))
        break

for port in range(port_minimum, port_maximum + 1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.2)
        s.connect((ip_add_entered, port))
        open_port.append(port)
    except:
        pass

for port in open_port:
    print(f"Port {port} is open on {ip_add_entered}.")
