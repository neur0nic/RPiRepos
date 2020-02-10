import RPi.GPIO as G
from time import sleep

G.setmode(G.BCM)
G.setwarnings(0)

G.setup(22, G.IN, pull_up_down=G.PUD_DOWN)
G.setup(18, G.OUT)
p = G.PWM(18, 100)
p.start(0)


def button():
    while not G.input(22):
        buzz()
        sleep(0.1)
    print('Pushed')
    return True


def buzz():
    for j in [50, 100]:
        p.ChangeDutyCycle(j)
        sleep(0.1)
        p.ChangeDutyCycle(0)
        sleep(0.5)


if __name__ == '__main__':
    for i in range(1, 5):
        button()
    print('Test exited successfully.')
    G.cleanup()
    exit()