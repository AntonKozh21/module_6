class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, _cords, speed):
        self._cords = _cords
        self.speed = speed


    def move(self, dx, dy, dz):
        new_x = self._cords[0] + dx * self.speed
        new_y = self._cords[1] + dy * self.speed
        new_z = self._cords[2] + dz * self.speed
        if new_z < 0 and not isinstance(self, AquaticAnimal):
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] = new_x
            self._cords[1] = new_y
            self._cords[2] = new_z

    def get_cords(self):
        print(f"X: {int(self._cords[0])}, Y: {int(self._cords[1])}, Z: {int(self._cords[2])}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

class Bird:
    beak = True


    def lay_eggs(self):
        import random
        count_eggs = [1, 2, 3, 4]
        random_eggs = random.choice(count_eggs)
        if random_eggs > 1:
            print(f'Here are {random_eggs} eggs for you')
        else:
            print(f'Here is {random_eggs} eggs for you')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] -= abs(dz) / 2 * self.speed

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):

    def __init__(self, speed, _cords = [0, 0, 0], sound = 'Click-click-click'):
        Animal.__init__(self, _cords, speed)
        self.sound = sound

    def move(self, dx, dy, dz):
        Animal.move(self, dx, dy, dz)

    def dive_in(self, dz):
        super().dive_in(dz)

    def speak(self):
        print(self.sound)

    def lay_eggs(self):
        super().lay_eggs()

print(Duckbill.mro())

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