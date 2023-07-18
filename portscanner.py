import pyfiglet
import socket
import urllib.parse
from datetime import datetime

# port scanner banner
banner = pyfiglet.figlet_format("Port Scanner")
print(banner)

# user input
site = urllib.parse.urlparse(input("Site to be Scanned..."))
site_name = site.netloc


def single_port_scan():
    port = int(input("Enter the port number"))
    print("Scanning started at:" + str(datetime.now()))
    target = (site_name, port)
    create_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    create_socket.settimeout(1)
    result = create_socket.connect_ex(target)
    if result == 0:
        print("Port is open")
    else:
        print("Port is not open")
    create_socket.close()
    print("Scanning ended at:" + str(datetime.now()))


def all_port_scan():
    for port in range(0, 65536):
        target = (site_name, port)
        print("Scanning started at:" + str(datetime.now()))
        create_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        create_socket.settimeout(0.01)
        result = create_socket.connect_ex(target)
        if result == 0:
            print(f"Port {port} is open")
        else:
            pass
        create_socket.close()
        print("Scanning ended at:" + str(datetime.now()))


# scan type selection
scan_type = input("Single Port Scan(SP) / 2)All Port Scan(AP)").lower()
if scan_type == "sp":
    single_port_scan()
elif scan_type == "ap":
    all_port_scan()
else:
    print(f"Given option is invalid")
