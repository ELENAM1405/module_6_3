from random import randint


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self,speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        dx_1 = dx * self.speed
        dy_1 = dy * self.speed
        dz_1 = dz * self.speed
        if dz_1 < 0:
            print(" It's too deep , i can't dive :( " )
        else:
            self._cords = [dx_1,dy_1,dz_1]

    def get_cords(self):
        print(f' X:  {self._cords[0]} ', end=' ')
        print(f' Y:  {self._cords[1]} ', end=' ')
        print(f' Z:  {self._cords[2]} ')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        self._DEGREE_OF_DANGER = randint(1,4)
        print(f'Here are(is) {self._DEGREE_OF_DANGER} eggs for you')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self,dz):
        dz_2 = int(self._cords[2]-abs(dz)*0.5*self.speed)
        self._cords[2] = max(dz_2,0)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal,Bird,AquaticAnimal):
    sound = "Click-click-click"
    def __init__(self,speed):
        super().__init__(speed)

    def speak(self):
        print(f'{self.sound}')

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











