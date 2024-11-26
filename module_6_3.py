from random import randint
class Animal:#класс описывающий животных
    live = True
    sound = None # звук(изначально отсутствует)
    _DEGREE_OF_DANGER = 0 # степень опасности существа

    def __init__(self,_cords,speed):
        super().__init__(_cords,speed)
        self.cords = _cords
        self.cords = [0, 0, 0] # координаты в пространстве
        self.speed = speed # скорость передвижения существа

    def move(self, dx, dy, dz):
        self.cords = [dx, dy, dz]
        for i in range(len(self.cords)):
            self.cords[int(i)] * self.speed
            if dz == 0:
                print(''' It's too deep , i can't dive :( ''' )

    def get_cords(self):
        print(f' X:  {self.cords[0]} ')
        print(f' Y:  {self.cords[1]} ')
        print(f' Z:  {self.cords[2]} ')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            if self._DEGREE_OF_DANGER >= 5:
                print("Be careful, i'm attacking you 0_0")

class Bird(Animal):# класс описывающий птиц
    beak = True

    def lay_eggs(self):
        self._DEGREE_OF_DANGER = [randint(1,4) for x in range(1)]
        print(f'Here are(is) {self._DEGREE_OF_DANGER} eggs for you')

class AquaticAnimal(Animal):# класс описывающий плавающего животного
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz): # где dz изм-e коор-ы z в _cords(метод должен всегда уменьшать координату z)
        dz = self.speed / 2
        return abs(dz)

class PoisonousAnimal(Animal):# класс описывающий ядовитых животных
    _DEGREE_OF_DANGER = 8

class Duckbill(Animal):#класс описывающий утконоса
    sound = "Click-click-click" # звук, который издаёт утконос
    def

db = Duckbill(10)      # Bird, AquaticAnimal, PoisonousAnimal

#print(db.live)
#print(db.beak)

#db.speak()
#db.attack()

#db.move(1, 2, 3)
#db.get_cords()
#db.dive_in(6)
#db.get_cords()

#db.lay_eggs()










