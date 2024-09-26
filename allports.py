# Port-finder is an Open-source Python project by BINDAAS
# v0.1 it will check ALL Ports Total 65536 Combinations
import socket
import logging
import time

print ("""
 ____ ___ _   _ ____    _        _    ____
| __ )_ _| \ | |  _ \  / \      / \  / ___|
|  _ \| ||  \| | | | |/ _ \    / _ \ \___ \\
| |_) | || |\  | |_| / ___ \  / ___ \ ___) |
|____/___|_| \_|____/_/   \_\/_/   \_\____/  V0.1
A Faster Port Checker From 1-65535 port with Log-file
""")

class SConnect:

    def __init__(self, ip, port=None):
        self.ip = ip
        self.port = port
        self.address = (self.ip, self.port)
        self.s_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_connection.settimeout(0.3)

    def portscan(self):
        return self.s_connection.connect_ex(self.address)


def main():

    logging.basicConfig(filename="errlog.log", format="%(asctime)s : %(message)s")
    logging.info("Start")
    print("\nPlease insert an IP address (IPv4/6) that you want to scan for open and closed ports.")
    u_ip = input("\nTarget IP:>>> ")

    open_pcounter = 0
    closed_pcounter = 0

    # Open file to save the open ports
    with open("all_open_ports.txt", "w") as open_ports_file:
        if u_ip is not None:
            for p in range(601, 65536):  # You can adjust the port range here
                start_ptime = time.time()
                c = SConnect(u_ip, p)
                if c.portscan() == 0:
                    print(f"Port {p} is open")
                    open_ports_file.write(f"IP: {u_ip}, Port: {p} is open\n")  # Save to file
                    open_pcounter += 1
                else:
                    print(f"Port {p} is closed")
                    closed_pcounter += 1
                print("--- %s seconds ---" % (time.time() - start_ptime))
        else:
            print("Invalid input, terminating.\n")

        print(f"Total open ports: {open_pcounter}")
        print(f"Total closed ports: {closed_pcounter}")
        logging.info("Finished")


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
