# -*- coding: utf-8 -*- 

#프로그램 시작
	
print('')
print('--------------------------------------------------')
print('**  Welcome to FROGMON corp.')
print("**  Let's make it together")
print("**  ")
print('--------------------------------------------------')
print('')


import struct
from bluepy.btle import Scanner, DefaultDelegate, UUID, Peripheral

TARGET_UUID = "0000fe95-0000-1000-8000-00805f9b34fb"
target_dev = None    

#############################################
# Define scan callback
#############################################
class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Discovered device %s" % dev.addr)
        elif isNewData:
            print("Received new data from %s" % dev.addr)

#############################################
# Define notification callback
#############################################
class NotifyDelegate(DefaultDelegate):
    #Constructor (run once on startup)  
    def __init__(self, params):
        DefaultDelegate.__init__(self)
      
    #func is caled on notifications
    def handleNotification(self, cHandle, data):
         print("Notification : " + data.decode("utf-8"))

#############################################
# Main starts here
#############################################
scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)
cnt = 0
dev_str=''


for dev in devices:
    print("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
    for (adtype, desc, value) in dev.getScanData():
        # Check iBeacon UUID
        # 255 is manufacturer data (1  is Flags, 9 is Name)
        print("  (AD Type=%d) %s = %s" % (adtype, desc, value))
        if adtype is 2 and TARGET_UUID in value:
            cnt = cnt+1
            target_dev = dev
            print("%d) Device %s (%s), RSSI=%d dB" % (cnt, dev.addr, dev.addrType, dev.rssi))
            dev_str = "sensor%02d" % (cnt)

print("Close app")

