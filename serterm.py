import serial
import time
import sys
import signal

port = '/dev/ttyUSB0'
baud = 2400

def signal_handler(signal, frame):
  print " detected, ending session"
  ser.close()
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

ser = serial.Serial(port, baud, parity=serial.PARITY_EVEN, timeout = 2.5)

while True:
  cmd = raw_input("> ")
  ser.write(cmd + "\r\n")
  time.sleep(0.1)
  while (ser.inWaiting()):
    ret = ser.readline().rstrip()
    print ret



