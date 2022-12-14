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
        print("Jaguar " + self.name + str(self.age) + " " + self.sound)
        

animal = JungleAnimal(name= "as", age= 15, sound= "s")
animal.make_sound()

jaguar = Jaguar(name= "", age= 3, sound= "rr")
jaguar.print()