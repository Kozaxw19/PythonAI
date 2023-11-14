class Dinosaur:
    def about(self):
        print("I am a dinosaur")
    def about_myself(self):
        print("I will eat you")
class Egg(Dinosaur):
    def about(self):
        print("I am an egg")
    def about_myself(self):
        print("I'm just an egg")
class Hen(Egg):
    def about(self):
        print("I am a hen")
    def about_myself(self):
        print("I'm a little crazy")
class Chick(Hen):
    def about(self):
        print("I am a chick")
    def about_myself(self):
        print("I don't understand what I'm doing here")