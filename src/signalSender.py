# -*- coding: utf-8 -*- 

# 중복 실행 방지
from tendo import singleton
try:
    me = singleton.SingleInstance()
except :
    print("another process running!")
    exit()

#프로그램 시작	
import sys
import RPi.GPIO as GPIO
import time
import datetime

from frogmon.uLogger     import LOG
from frogmon.uCommon     import COM
from frogmon.uGlobal     import GLOB
from frogmon.uRequest    import REQUEST

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#GPIO LOC
METRIX_A = 2
METRIX_B = 3 

GPIO.setup(METRIX_A, GPIO.IN)
GPIO.setup(METRIX_B, GPIO.IN)

metrixA = 0
metrixB = 0

lstMetrixA = 99
lstMetrixB = 99

try:
    print("[CONTROL] : Singnal Sender Start !")
    while (True):
        time.sleep(1)
        metrixA = GPIO.input(METRIX_A)
        metrixB = GPIO.input(METRIX_B)
        if metrixA != lstMetrixA or metrixB != lstMetrixB :
            REQUEST.updateSignal(metrixA, metrixB)
            lstMetrixA = metrixA
            lstMetrixB = metrixB

finally:
    GPIO.cleanup()