his entrypoint file to be used in development. Start by reading README.md
import port_scanner
from unittest import main

# Called with URL
print("Scanning \"www.freecodecamp.org\"...")
ports = port_scanner.get_open_ports("www.freecodecamp.org", [75, 85])
print("Open ports:", ports, "\n")

# Called with ip address
print ("Scanning 104.26.10.78...")
ports = port_scanner.get_open_ports("104.26.10.78", [8079, 8090])
print("Open ports:", ports, "\n")

# Verbose called with ip address and no host name returned -- single open port
print ("Scanning 104.26.10.78...")
ports = port_scanner.get_open_ports("104.26.10.78", [440, 450], True)
print("Open ports:",ports, "\n")

# Verbose called with ip address and valid host name returned -- single open port
print ("Scanning 137.74.187.104...")
ports = port_scanner.get_open_ports("137.74.187.104", [440, 450], True)
print("Open Ports:", ports, "\n")

# Verbose called with host name -- multiple ports returned
print ("Scanning scanme.nmap.org...")
ports = port_scanner.get_open_ports("scanme.nmap.org", [20, 80], True)
print("Open ports:" ,ports, "\n")

# Run unit tests automatically
#main(module = "test_module", exit = False)
