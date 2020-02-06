import RPi.GPIO as G
from time import sleep

G.setmode(G.BCM)
G.setwarnings(0)

G.setup(18, G.OUT)
p = G.PWM(18, 100)
p.start(0)

if __name__ == '__main__':
    for i in [50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100]:
        p.ChangeDutyCycle(i)
        sleep(0.1)
        p.ChangeDutyCycle(0)
        sleep(0.5)
    p.stop()
    print('Test exited successfully.')
    G.cleanup()
    exit()
