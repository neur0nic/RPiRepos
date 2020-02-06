import RPi.GPIO as G
from time import sleep

G.setmode(G.BCM)
G.setwarnings(0)

G.setup(22, G.IN, pull_up_down=G.PUD_UP)


if __name__ == '__main__':
    for i in range(1,6):
        while G.wait_for_edge(22, G.FALLING):
            sleep(0.1)
        print('Pushed')
    print('Test exited successfully.')
    G.cleanup()
    exit()