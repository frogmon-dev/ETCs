"""
A simple Python script to receive messages from a client over
Bluetooth using PyBluez (with Python 2).
"""

import bluetooth

hostMACAddress = 'E4:5F:01:65:6C:05' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
#hostMACAddress = 'B8:27:EB:FA:42:AB' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 3
backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)
try:
    client, clientInfo = s.accept()
    print("Accepted connection from ", clientInfo)
    while 1:
        data = client.recv(size)
        if data:
            #print(data)
            print("Received: %s" % data)
            client.send(data) # Echo back to client
except:	
    print("Closing socket")
    client.close()
    s.close() 