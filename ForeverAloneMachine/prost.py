import RPi.GPIO as GPIO
from time import time, sleep, strftime

'''
The Forever-Alone-Machine Mark II gives you someone to toast, even if you are alone or the other one is somewhere else
on the world.

Written and tested on a Raspberry Pi B+
'''

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)


def klink(pin):
    '''
    Moves the glas with an servomotor
    :param pin: GPIO 18 preferred
    :return:
    '''
    GPIO.setup(pin, GPIO.OUT)
    p = GPIO.PWM(pin, 1000)     # Frequenzy must be adjusted to the motor
    up = 0      # DutyCycle for the upright position
    down = 50   # DutyCycle for the full tilt position
    p.start(up)
    for i in range(up, (down + 5), 5):
        p.ChangeDutyCycle(i)
        sleep(0.05)
    sleep(0.75)
    for i in range(down, (up -5), -5):
        p.ChangeDutyCycle(i)
        sleep(0.05)


def button(pin):
    '''
     Waiting for the button to be pushed
    :return: True
    :param pin:
    '''
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.wait_for_edge(pin, GPIO.FALLING)
    return True


def add_to_log(errormessage):
    """ For writing an Error.log file
        Creates a log-file with time and error message
        :param errormessage:    the error message; str
    """
    if isinstance(errormessage, str):
        time = strftime("%Y-%m-%d: %H:%M:%S - ")
        with open('Error.log', 'a') as fa:
            fa.write(time + errormessage)
    else:
        pass


def mode_one():
    '''
    For drinking home alone
    :return:
    '''
    while True:
        button(2)
        klink(18)
        sleep(30)


def mode_two():
    '''
    Connects to another FAMM2 and toast when both buttons are activated
    :return:
    '''
    pass


if __name__ == '__main__':
    modeOne()
    GPIO.cleanup()
    exit()