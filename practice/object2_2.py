# カプセル化

class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def describe(self):
        print("name: {}; age{}; height: {};".format(name, age, height))

    def introduce(self):
        print("my name is {}, and height is {}, and age is {}. ".format(name, age, height))
