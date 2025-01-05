import random

class Animal:
    def __init__(self, speed):
        self.live = True
        self.sound = None
        self._DEGREE_OF_DANGER = 0
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if self._cords[2] < 0:
            print("It's too deep, i can't dive :(")
            pass
        _list = [dx,dy,dz]
        cords = []
        for i in _list:
            new_cords = i * self.speed
            cords.append(new_cords)
        self._cords = cords
    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):

        if self._DEGREE_OF_DANGER < 5:
            print(f"Sorry, i'm peaceful :)")
        if self._DEGREE_OF_DANGER >= 5:
            print(f"Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self.beak = True
    def lay_eggs(self):
        print(f"Here are(is) {random.randint(1, 4)} egg(s) for you!")

class AquaticAnimal(Animal):
    def __init__(self,speed):
        super().__init__(speed)
        _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] = self._cords[2] - abs(dz)
        self.speed = self.speed / 2

class PoisonousAnimal(Animal):
    def __init__(self,speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    def __init__(self,speed):
        super().__init__(speed)
        self.sound = 'Click-click-click'

# Пример работы программы:

db = Duckbill(10)
print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)

db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()