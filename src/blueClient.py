"""
A simple Python script to send messages to a sever over Bluetooth
using PyBluez (with Python 2).
"""

import string
import bluetooth
import time

serverMACAddress = 'E4:5F:01:65:6C:05'
port = 1
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))
cnt = 0
while 1:
    data = s.recv(1024)
    if len(data) > 0:
        print("Received: %s" %data)
    else:
        cnt = cnt + 1
        text = '%d' % cnt
        time.sleep(1) 
        #raw_input() # Note change to the old (Python 2) raw_input
        s.send(text)
s.close()