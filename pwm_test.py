import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

GPIO.output(22, 0)
GPIO.output(23, 0)
GPIO.output(24, 0)



r = GPIO.PWM(22, 100)
g = GPIO.PWM(23, 100)
b = GPIO.PWM(24, 100)


r.stop()
g.stop()
b.stop()

#p.start(50)


r.start(0)
g.start(0)
b.start(0)

period = 1000   #ms
step = 1 

'''
try:
    while 1:
        for dc in range(0, 101, 1):
            r.ChangeDutyCycle(dc)
            g.ChangeDutyCycle(dc)
            b.ChangeDutyCycle(dc)
            #p.ChangeFrequency(dc)
            time.sleep(0.01)
        for dc in range(100, -1, -1):
            r.ChangeDutyCycle(dc)
            g.ChangeDutyCycle(dc)
            b.ChangeDutyCycle(dc)
            #p.ChangeFrequency(dc)
            time.sleep(0.01)
except KeyboardInterrupt:
    pass
'''

delay = 0.01

try:
    while 1:
        #000 -> 100
        for v in range(0, 101, 1):
            r.ChangeDutyCycle(v)
            time.sleep(delay)
        #
        #100 -> 110
        for v in range(0, 101, 1):
            g.ChangeDutyCycle(v)
            time.sleep(delay)
        #
        #110 -> 010
        for v in range(100, -1, -1):
            r.ChangeDutyCycle(v)
            time.sleep(delay)
        #
        #010 -> 011
        for v in range(0, 101, 1):
            b.ChangeDutyCycle(v)
            time.sleep(delay)
        #
        #011 -> 001
        for v in range(100, -1, -1):
            g.ChangeDutyCycle(v)
            time.sleep(delay)
        #
        #001 -> 101
        for v in range(0, 101, 1):
            r.ChangeDutyCycle(v)
            time.sleep(delay)
        #
        #101 -> 111
        for v in range(0, 101, 1):
            g.ChangeDutyCycle(v)
            time.sleep(delay)
        #
        
        ###REVERSE THE ORDER HERE
        ##for now just stop
        r.ChangeDutyCycle(0)
        b.ChangeDutyCycle(0)
        g.ChangeDutyCycle(0)
    #
except KeyboardInterrupt:
    pass
#
#


r.stop()
g.stop()
b.stop()

GPIO.cleanup()
