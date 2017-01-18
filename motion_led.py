#!/usr/local/bin/python2.7

import pyfirmata
from time import sleep
import sys, signal

def signal_handler(signal, frame):
    print
    board.exit()
    sys.exit(0)


def blinkLED(pin, message):
    print message
    board.digital[pin].write(1)
    sleep(1)
    board.digital[pin].write(0)
    sleep(1)
    pass

port = '/dev/ttyACM0'
board = pyfirmata.Arduino(port)


it = pyfirmata.util.Iterator(board)
it.start()

pirPin = board.get_pin('d:7:i')
redPin = 12
greenPin = 13

board.digital[redPin].write(1)
board.digital[greenPin].write(1)

# http://stackoverflow.com/questions/18994912/ending-an-infinite-while-loop

signal.signal(signal.SIGINT, signal_handler)

while True:
    value = pirPin.read()

    if value is True:
        board.digital[greenPin].write(1)
        blinkLED(redPin, "Motion detected")
    elif value is False:
        board.digital[redPin].write(1)
        blinkLED(greenPin, "No motion detected")


