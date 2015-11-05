from energenie import switch_on, switch_off
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN, GPIO.PUD_UP)

switch_off()

try:
    while True:
        if GPIO.input(20) == 1:     
            switch_on()
            time.sleep(30)
            switch_off()
        else:
            switch_off()
except KeyboardInterrupt:
    print("EXIT")
    switch_off()

