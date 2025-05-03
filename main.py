import socket
import datetime
import time

print("For educational purpose only")
# ````
# A Tool made for education purpose.
# Please use it for learning only
# Happy hacking
# ``````
target = input("Please Enter the ip address : ")

def portScan(target):
    try:
        ip  = socket.gethostbyname(target)
        
        print(f"Scanning the target {ip} ..")
        print("time started", datetime.datetime.now())

        for port in range(20,90):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip,port))

            if result ==0:
                print("Port open {}".format(port))
            sock.close()
    except socket.gaierror:
        print("Host name could not be resolved .")

    except socket.error:
        print("could not connect to host")
    
    except KeyboardInterrupt:
        print("Quiting the scan ..")

portScan(target)


