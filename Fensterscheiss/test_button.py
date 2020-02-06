import RPi.GPIO as G

G.setmode(G.BCM)
G.setwarnings(0)

G.setup(22, G.IN, pull_up_down=G.PUD_DOWN)


def button():
    while not G.input(22):
        pass
    print('Pushed')
    return True


if __name__ == '__main__':
    button()
    print('Test exited successfully.')
    G.cleanup()
    exit()