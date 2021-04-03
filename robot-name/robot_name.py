from string import ascii_uppercase
from random import randint, seed, choice
class Robot:
    "This is a Robot class"
    name = ""
    def __init__(self):
        self.name = self.get_randName()

    def reset(self):
        self.name = self.get_randName()

    def get_randName(self):
        seed()
        return ''.join(choice(ascii_uppercase) for i in range(2)) + ''.join(str(randint(0, 9)) for num in range(0, 3))