#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import random
pinRojo = 21
pinVerde = 20
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup([pinRojo,pinVerde],GPIO.OUT)

def rojo():
    tiempo = True
    contador = 0
    while tiempo:
        GPIO.output(20,GPIO.LOW)
        GPIO.output(21,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(21,GPIO.LOW)
        time.sleep(0.1)
        contador += 1
        if contador >= 5:
            tiempo = False


def verde():
    GPIO.output(20,GPIO.HIGH)
    GPIO.output(21,GPIO.LOW)
rojo()
verde()
print("Saludos.....")
print("Javi....")
