class Cat:
    print("Hi!")

    def __init__(self, name):
        self.name = name
        self.hungry = True
        self.joyful = False

    def feed(self):
        if not self.hungry:
            print(f"{self.name} isn't hungry.")
        else:
            print(f"{self.name} has been fed.")
            self.hungry = False

    def play(self):
        if self.joyful:
            print(f"{self.name} is already playing.")
            self.hungry = False
        else:
            print(f"{self.name} is playing now.")
            self.joyful = True


