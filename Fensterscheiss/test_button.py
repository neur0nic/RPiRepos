import RPi.GPIO as G

G.setmode(G.BCM)
G.setwarnings(0)

G.setup(22, G.IN, pull_up_down=G.PUD_DOWN)

if __name__ == '__main__':
    while True:
        if G.input(22) == G.HIGH:
            print("Button was pushed!")
    G.cleanup()
    exit()