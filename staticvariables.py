from telnetlib import DO


class Dog:
    numofDogs = 0
    def __init__(self, name="unknown"):
        self.name = name
        Dog.numofDogs += 1

    @staticmethod
    def getnumofDogs():
        print("There are {} dogs".format(Dog.numofDogs))
def main():
    spot = Dog("Spot")
    doug = Dog("doug")
    spot.getnumofDogs()
main()