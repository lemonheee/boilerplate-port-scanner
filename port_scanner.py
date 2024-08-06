import socket

def get_open_ports(target, port_range, verbose = False):
    open_ports = []

  if verbose == True:
        print("Port    Service")

    for scan_port in range(port_range[0], port_range[1]+1):
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target,scan_port))
        if result ==0:
            #print(f" port {scan_port} is  open ")
            open_ports.append ( scan_port )
            if verbose == True:
                port_v= scan_port
                service_v= common_ports.ports_and_services[scan_port]
                print (port_v, "    ",service_v)

    return(open_ports)
