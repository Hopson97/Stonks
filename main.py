from os import system, name
from time import sleep
from random import randrange

def clear(): 
    print(chr(27) + "[2J")

class Buffer:
    def __init__(self):
        self.buff = []
        self.width = 125
        self.height = 54
        for _ in range(self.height):
            for _ in range(self.width):
                self.buff += '.'
            self.buff += '\n'
        for y in range(self.height):
            val = str(self.height - y)
            if len(val) > 1:
                self.buff[y * self.width + y] = val[0]
                self.buff[y * self.width + y + 1] = val[1]
            else:
                self.buff[y * self.width + y] = val
        
    def set(self, x, y, v):
        self.buff[y * self.width + y + x] = v

    def print(self):
        print("".join(self.buff))

    def clear(self):
        for y in range(self.height):
            for x in range(3, self.width):
                self.set(x, y, ' ')
            
class Stonk:
    def __init__(self, start):
        self.history = []
        self.value = start 

    def sim(self):
        self.history.append(self.value)
        if randrange(0, 10) > 3:
            self.value += 1 
        else:
            self.value -= 1
        self.value = max(0, self.value)


buffer = Buffer()
stonk = Stonk(0)
buffer.clear()

while True:
    sleep(0.25)
    for idx, value in enumerate(stonk.history):
        buffer.set(idx + 3, buffer.height - value - 1, '#')

    stonk.sim()
    buffer.print()

    buffer.clear()

