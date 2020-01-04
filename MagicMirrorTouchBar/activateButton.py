import RPi.GPIO as GPIO
from time import sleep
'''
Written and tested on the Raspberry Pi B+
'''


def pulsLED(pin):
    '''
    Lets the LED pulsate.
    :param pin: GPIO the anode of the LED is on
    :return:
    '''
    GPIO.setup(pin, GPIO.OUT)
    p = GPIO.PWM(pin, 100)    # GPOI 18 with 100Hz -> T=10ms
    p.start(0)
    #t = [50, 60, 70, 80, 90, 100, 80, 60, 50, 60, 80, 100, 80, 60, 50, 60, 80, 100, 80, 60, 50, 60, 80, 70, 60, 50]
    #t = [10, 20, 30, 40, 50, 45, 35, 45, 50, 45, 35, 45, 50, 45, 35, 45, 50, 45, 35, 45, 50, 40, 30, 20, 10]
    t = [15, 30, 45, 60, 75, 90, 100, 80, 60, 40, 60, 80, 100, 80, 60, 40, 60, 80, 100, 90, 75, 60, 45, 30, 15, 0]
    for i in t:
        p.ChangeDutyCycle(i)
        sleep(0.1)
    p.stop()


if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    pin = [18, 23, 25]
    for i in pin:
        pulsLED(i)
    GPIO.cleanup()
    exit()