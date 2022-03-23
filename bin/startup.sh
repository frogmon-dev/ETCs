#!/bin/bash

echo "process start"

#sudo python3 /home/pi/ETCs/src/signalSender.py &

#sudo python3 /home/pi/ETCs/src/fireWarn.py &

sudo bluetoothctl <<EOF
power on
discoverable on
pairable on
EOF

sudo hciconfig hci0 sspmode 0
sudo bt-agent -c NoInputNoOutput -p /root/bluetooth.cfg &
