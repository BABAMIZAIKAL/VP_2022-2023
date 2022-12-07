import random

class InvalidParameterError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__("Invalid class parameter: " + self.message)

class MissingParameterError(Exception):
    def __init__(self):
        super().__init__("Missing parameter error ")

class InvalidAgeError(InvalidParameterError):
    def __init__(self):
        super().__init__("age")

class InvalidSoundError(InvalidParameterError):
    def __init__(self):
        super().__init__("sound")

class JungleAnimal:
    def __init__(self, name = None, age = None, sound = None):
        if name is None or age is None or sound is None:
            raise MissingParameterError
        if type(name) != str:
            raise InvalidParameterError("name")
        if type(age) != int:
            raise InvalidAgeError()
        if type(sound) != str:
            raise InvalidSoundError()
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(self.name + " says " + self.sound + "!")
    
    def print(self):
        pass

    def daily_task(self):
        pass

class Jaguar(JungleAnimal):
    def __init__(self, name=None, age=None, sound=None):
        super().__init__(name, age, sound)
        if age > 15:
            raise InvalidAgeError()
        if sound.count("r") < 2:
            raise InvalidSoundError()
    def print(self):
        print("Jaguar(" + self.name + ", " + str(self.age) + ", " + self.sound + ")")

    def daily_task(self, listAnimals):
        string = ""
        for i in listAnimals:
            if type(i) == Lemur or type(i) == Human:
                string = (self.name + " the Jaguar hunted down " + i.name + " the " + str(i.__class__.__name__))
                listAnimals.remove(i)
                break
        print(string)
        

class Lemur(JungleAnimal):
    def __init__(self, name=None, age=None, sound=None):
        super().__init__(name, age, sound)
        if age > 10:
            raise InvalidAgeError()
        if sound.count("e") < 1:
            raise InvalidSoundError()
    def print(self):
        print("Lemur(" + self.name + ", " + str(self.age) + ", " + self.sound + ")")
    def daily_task(self, count):
        if count <= 0:
            self.make_sound()
            self.make_sound()
            return 0
        elif count >= 10:
            print(self.name + " the Lemur ate a full meal of 10 fruits")
            count = count - 10
            return count
        elif count < 10:
            print(self.name + " the Lemur could only find " + str(count) + "fruits")
            count = 0
            return count
    def make_sound(self):
        print(self.name + " the Lemur couldn't find anything to eat")

class Human(JungleAnimal):
    def __init__(self, name=None, age=None, sound=None):
        super().__init__(name, age, sound)
        if age > 10:
            raise InvalidAgeError()
        if sound.count("e") < 1:
            raise InvalidSoundError()
    def print(self):
        print("Human(" + self.name + ", " + str(self.age) + ", " + self.sound + ")")

    def daily_task(self, listAnimals, listBuildings):
        x = listAnimals.index(self)
        if x == 0:
            if type(listAnimals[1]) == Human:
                listBuildings.append(Building(type="asdf"))
        elif x == (len(listAnimals) - 1):
            if type(listAnimals[(len(listAnimals)-2)]) == Human:
                listBuildings.append(Building(type="asdf"))
        else:
            if type(listAnimals[x-1]) == Human and type(listAnimals[x+1]):
                listBuildings.append(Building(type="asdf"))

class Building:
    def __init__(self, type):
        self.type = type
        

# animal = JungleAnimal(name= "as", age= 15, sound= "s")
# animal.make_sound()

# jaguar = Jaguar(name= "Jaguar", age= 3, sound= "rr")
# jaguar.print()
# jaguar.daily_task([Lemur(name="lemur", age=10, sound="e")])

fruits = 100
animals = []
buildings = []

names = [
    "Jacob",
    "David",
    "Bobby",
    "Steve",
    "Johanssen",
    "Mac",
    "Jason",
    "Edward",
    "Alex",
    "Maddie",
    "Susan",
    "Abigail",
    "Jessica",
    "Lizzy",
    "Monica",
    "Lorelei",
    "Sandra",
    "Michelle"
]

sounds = [
    "RAAWR",
    "ROAR",
    "Grrr",
    "Shriek",
    "Meow",
    "Eeek",
    "Aaaaa",
    "Speak",
    "I am a Human"
]

for i in range(102):
    num = random.randint(0, 10)
    if num in range(0,4):
        animals.append(Lemur(name=("Lemur" + str(i)), age= 5, sound= "rrsseess"))
    elif num in range(4,8):
        animals.append(Jaguar(name=("Jaguar" + str(i)), age= 5, sound= "rrsseess"))
    elif num in range(8, 10):
        animals.append(Human(name=("Human" + str(i)), age= 5, sound= "rrsseess"))

print(f"The jungle now has {len(animals)} animals")


for anim in animals:
    if type(anim) == Lemur:
        fruits = anim.daily_task(count= fruits)
    elif type(anim) == Human:
        anim.daily_task(listAnimals= animals, listBuildings = buildings)
    else:
        anim.daily_task(listAnimals= animals)


print(f"The jungle now has {len(animals)} animals")
print(fruits)
print(animals)
print(buildings)
