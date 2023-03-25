"""
参考:
------
https://qiita.com/kaitolucifer/items/926ed9bc08426ad8e835
"""

# 鳥, 犬, 魚のclass ########################################
class Bird:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("the bird named {} is flying".format(self.name))

class Dog:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("the dog named {} is running".format(self.name))

class Fish:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("the fish named {} is swimming".format(self.name))

############################################################

if __name__ == "__main__":

    bob = Bird("Bob")
    john = Bird("John")
    david = Dog("David")
    fabian = Fish("Fabian")

    bob.move()
    john.move()
    david.move()
    fabian.move()

