"""
A simple Python script to send messages to a sever over Bluetooth
using PyBluez (with Python 2).
"""

import string
import bluetooth

serverMACAddress = 'E4:5F:01:65:6C:05'
port = 3
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))
cnt = 0
while 1:
    cnt = cnt + 1
<<<<<<< HEAD
    text = '%d' % cnt
=======
    text = string(cnt)
>>>>>>> 1201f22f7688a846648e31d60464d43be2fcfb0c
    sleep(1) 
    #raw_input() # Note change to the old (Python 2) raw_input
    if text == "quit":
        break
    s.send(text)
s.close()