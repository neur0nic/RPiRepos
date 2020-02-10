import RPi.GPIO as G
from time import sleep
from os import system

G.setmode(G.BCM)
G.setwarnings(0)

LED = 2
G.setup(LED, G.OUT)
Button = 22
G.setup(Button, G.IN, pull_up_down=G.PUD_DOWN)
Buzzpin = 18
G.setup(Buzzpin, G.OUT)


def blink():
    for i in range(1, 4):
        G.output(LED, G.HIGH)
        sleep(0.5)
        G.output(LED, G.LOW)
        sleep(0.5)


def countdown():
    for i in range(1, 10):
        print(i)
        sleep(60)
        blink()
    pass


def button(fnktn):
    while not G.input(22):
        fnktn


def buzzer():
    p = G.PWM(Buzzpin, 100)
    p.start(0)
    while True:
        p.ChangeDutyCycle(50)
        sleep(0.2)
        p.ChangeDutyCycle(0)
        sleep(0.5)
        p.ChangeDutyCycle(100)
        sleep(0.2)
        p.ChangeDutyCycle(0)
        sleep(0.5)


if __name__ == '__main__':
    print('Program started')
    blink()
    countdown()
    print('Countdown ended')
    button(buzzer())
    blink()
    print('Ready to shutdown')
    system('systemctl poweroff')
    #G.cleanup()
    exit()