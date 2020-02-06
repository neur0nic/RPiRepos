import RPi.GPIO as G
from time import sleep

G.setmode(G.BCM)
G.setwarnings(0)

G.setup(2, G.OUT)

if __name__ == '__main__':
    for i in range(1,21):
        G.output(2, G.HIGH)
        sleep(0.5)
        G.output(2, G.LOW)
        sleep(0.5)
    print('Test exited successfully.')
    exit()