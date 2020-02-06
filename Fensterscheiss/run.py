import RPi.GPIO as G
from time import sleep
from os import system

G.setmode(G.BCM)
G.setwarnings(0)

LED = 2
G.setup(LED, G.OUT)
Button = 22
Buzzpin = 18


def blink():
    for i in range(1, 4):
        G.output(LED, G.HIGH)
        sleep(0.5)
        G.output(LED, G.LOW)
        sleep(0.5)


def countdown():
    for i in range(1, 11):
        sleep(60)
        blink()
    pass


def button(pin):
    G.setup(pin, G.IN, pull_up_down=G.PUD_UP)
    G.wait_for_edge(pin, G.FALLING)
    return True


def buzzer():
    pass


if __name__ == '__main__':
    blink()
    countdown()
    buzzer()
    blink()
    system('systemctl poweroff')
    exit()