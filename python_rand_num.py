#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 12:40:34 2018

@author: jerry
"""

import serial


# this port address is for the serial Arduino port
SERIAL_PORT = '/dev/cu.usbmodem1411'
#the same rate used on the Arduino
SERIAL_RATE = 9600


def main():
    ser = serial.Serial(SERIAL_PORT, SERIAL_RATE, timeout=1)
    guess = input("Guess a number between 1 and 10000\n")
    ser.write(str(guess).encode('ascii'))
    while True:
        # using ser.readline() assumes each line contains a single reading
        # sent using Serial.println() on tdshe Arduino
        while not ser.inWaiting():
            pass
        reading = str(ser.readline().decode('utf-8')).rstrip("\n").rstrip("\r")
        # reading is a string
        
        if reading == 'Guess is correct.':
            print("Congratulations! \n")
            print(reading + "\n")
            while not ser.inWaiting():
                pass
            reading = ser.readline().decode('utf-8')
            print("Total number of guesses: " + reading + "\n")
            break
        else:
            print(reading)
            guess = input("Try again. \n")
            ser.write(str(guess).encode('ascii'))
    
    ser.close()
    
if __name__ == "__main__":
    main()