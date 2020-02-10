import RPi.GPIO as G
from time import sleep, strftime
from os import system

G.setmode(G.BCM)
G.setwarnings(0)

LED = 2
G.setup(LED, G.OUT)
Button = 22
G.setup(Button, G.IN, pull_up_down=G.PUD_DOWN)
Buzzpin = 18
G.setup(Buzzpin, G.OUT)
p = G.PWM(Buzzpin, 100)


def blink():
    for i in range(1, 4):
        G.output(LED, G.HIGH)
        sleep(0.5)
        G.output(LED, G.LOW)
        sleep(0.5)


def countdown():
    for i in range(1, 10):
        #print(i)
        sleep(60)
        blink()
    pass


def button():
    while not G.input(22):
        buzz()
        sleep(0.05)
    print('Pushed')
    return True


def buzz():
    for j in [50, 100]:
        p.ChangeDutyCycle(j)
        sleep(0.2)
        p.ChangeDutyCycle(0)
        sleep(0.5)


def add_to_log(logmessage):
    """ Creates a log-file with time and message
        :param logmessage:    the error message; str
    """
    if isinstance(logmessage, str):
        time = strftime("%Y-%m-%d: %H:%M:%S - ")
        with open('Fensterscheiss.log', 'a') as fa:
            fa.write(time + logmessage)
    else:
        pass


if __name__ == '__main__':
    add_to_log('Program started')
    blink()
    countdown()
    #print('Countdown ended')
    p.start(0)
    button()
    blink()
    add_to_log('Ready to shutdown')
    system('systemctl poweroff')
    #G.cleanup()
    exit()