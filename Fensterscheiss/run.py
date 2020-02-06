import RPi.GPIO as G
from time import sleep
from os import system

G.setmode(G.BCM)
G.setwarnings(0)

LED = 2
G.setup(LED, G.OUT)
Button = 22
G.setup(Button, G.IN, pull_up_down=G.PUD_UP)
Buzzpin = 18
G.setup(Buzzpin, G.OUT)


def blink():
    for i in range(1, 4):
        G.output(LED, G.HIGH)
        sleep(0.5)
        G.output(LED, G.LOW)
        sleep(0.5)


def countdown():
    for i in range(1, 11):
        print(i + ' Min.')
        sleep(10)       # Changed from 60s to 10s for debugging
        blink()
    pass


def button():
    G.wait_for_edge(Button, G.FALLING)
    return True


def buzzer():
    p = G.PWM(Button, 100)
    p.start(0)
    while not button():
        p.ChangeDutyCycle(50)
        sleep(1)
        p.ChangeDutyCycle(100)
        sleep(1)


if __name__ == '__main__':
    print('Program started')
    blink()
    countdown()
    print('Countdown ended')
    buzzer()
    blink()
    print('Ready to shutdown')
    system('systemctl poweroff')
    exit()