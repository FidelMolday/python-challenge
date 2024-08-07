class animal:
    food = ""
    def makenoise(self):
        pass

class pet():
    def bepetted(self):
        print("pet me")

class canine():
    def shownails(self):
        print("My nails are long")

class dog(pet):
    def __init__(self):
        print("I am a dog")
        self.food = "bone"
    def makenoise(self):
        print("woof!")

class cat(pet,canine):
    def __init__(self):
        self.food = "milk"
        print("I am a cat")
    def makenoise(self):
        print("meow!")                                        