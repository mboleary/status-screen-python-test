#!/usr/bin/python3
# Testing Serial in Python

import serial
import time

WIDTH = 160
HEIGHT = 128

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=100) #115200

ser.setDTR(False) # Resets Arduino

time.sleep(1)

ser.flushInput()

ser.setDTR(True)

MAX = WIDTH * HEIGHT * 2
# MAX = 160 * 2

time.sleep(5)

LO_MAX = 31
HI_MAX = 248

with ser:
    ser.write(b'A') # Opcode to Draw Pixels on the screen
    print("Writing Color Bytes...")
    for i in range(0, WIDTH):
        for j in range(0, HEIGHT):
            if (i <= j):
                lo = 255
                hi = 255
            else:
                # lo = i % 256
                # hi = j % 256
                lo = LO_MAX
                hi = HI_MAX
            print(i, j, ":", lo, hi)
            ser.write(bytes([lo, hi]))
            # Serial Data isn't always read in immediately after writing
    print("Writing End Byte")
    ser.write(b"\n")
    time.sleep(2)
    print("Reading Serial Data...")
    ba = bytearray()
    while(ser.in_waiting):
        val = ser.read() # Reads one byte
        ba.extend(val) 
    print("End:", ba)
    ser.close()