from os import system, name
from time import sleep
from random import randrange

WIDTH = 175
HEIGHT = 54

STONKS = "\n\
                _____ _______ ____  _   _ _  __ _____    _____ _____ __  __ _    _ _            _______ ____  _____  TM \n\
               / ____|__   __/ __ \| \ | | |/ // ____|  / ____|_   _|  \/  | |  | | |        /\|__   __/ __ \|  __ \ \n\
              | (___    | | | |  | |  \| | ' /| (___   | (___   | | | \  / | |  | | |       /  \  | | | |  | | |__) |\n\
               \___ \   | | | |  | | . ` |  <  \___ \   \___ \  | | | |\/| | |  | | |      / /\ \ | | | |  | |  _  / \n\
               ____) |  | | | |__| | |\  | . \ ____) |  ____) |_| |_| |  | | |__| | |____ / ____ \| | | |__| | | \ \ \n\
              |_____/   |_|  \____/|_| \_|_|\_\_____/  |_____/|_____|_|  |_|\____/|______/_/    \_\_|  \____/|_|  \_\ \n"

class Buffer:
    def __init__(self):
        self.buff = []
        for _ in range(HEIGHT):
            for _ in range(WIDTH):
                self.buff += '.'
            self.buff += '\n'
        for y in range(HEIGHT):
            val = str(HEIGHT - y)
            if len(val) > 1:
                self.buff[y * WIDTH + y] = val[0]
                self.buff[y * WIDTH + y + 1] = val[1]
            else:
                self.buff[y * WIDTH + y] = val
        
    def set(self, x, y, v):
        self.buff[y * WIDTH + y + x] = v

    def print(self):
        print("".join(self.buff))

    def clear(self):
        for y in range(HEIGHT):
            for x in range(3, WIDTH):
                self.set(x, y, '.')
            
class Stonk:
    def __init__(self, start):
        self.history = []
        self.value = start 

    def sim(self):
        self.history.append(self.value)
        if randrange(0, 1000) > 333:
            self.value += 1 
        else:
            self.value -= 1
        self.value = max(0, self.value)
        self.value = min(HEIGHT - 1, self.value)


buffer = Buffer()
stonk = Stonk(0)
buffer.clear()
while len(stonk.history) < WIDTH - 3:
    sleep(0.01)
    print(STONKS)
    for idx, value in enumerate(stonk.history):
        buffer.set(idx + 3, HEIGHT - value - 1, '#')
    stonk.sim()
    buffer.print()


