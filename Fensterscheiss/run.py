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
G.setup(Buzzpin, G.PWM)


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


def button():
    G.wait_for_edge(Button, G.FALLING)
    return True


def buzzer():
    p = G.PWM(Button, 200)
    p.start(0)
    while not button():
        p.ChangeDutyCircle(50)
        sleep(1)
        p.ChangeDutyCircle(100)
        sleep(1)


if __name__ == '__main__':
    blink()
    countdown()
    buzzer()
    blink()
    system('systemctl poweroff')
    exit()