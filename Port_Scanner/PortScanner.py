# using nmap
import nmap
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
    port_range = input("Enter a port range(e.g. start-end):   ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ", ""))
    if port_range_valid:
        port_minimum = int(port_range_valid.group(1))
        port_maximum = int(port_range_valid.group(2))
        break

nm = nmap.PortScanner()
for port in range(port_minimum, port_maximum + 1):
    try:
        result = nm.scan(ip_add_entered, str(port))
        port_status = (result['scan'][ip_add_entered]['tcp'][port]['state'])
        print(f"Port {port} is {port_status}")

    except:
        print(f"Cannot scan port {port}.")
