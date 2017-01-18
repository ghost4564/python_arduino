import serial
import time
import sys
import signal

port = '/dev/ttyUSB1'
baud = 2400

def signal_handler(signal, frame):
  print " detected, ending session"
  ser.close()
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

ser = serial.Serial(port, baud, parity=serial.PARITY_EVEN, timeout = 2.5)

while True:
  while (ser.inWaiting()):
    ret = ser.readline().rstrip()
    print ret



