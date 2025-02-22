class Hero: # template
    # class variable
    jumlah_hero = 0

    def __init__(self,inputName,inputHealth,inputPower,inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1
    
    # void function, method tanpa return, tanpa argument
    def siapa(self):
        print("Namaku adalah : ", self.name)

    # method dengan argument, tanpa return
    def healthup(self,up):
        self.health += up

    # method dengan return
    def getHealth(self):
        return self.health


hero1 = Hero("Miya", 60, 80, 20)
hero2 = Hero("Lukas", 70, 70, 30)
hero3 = Hero("Lolita", 80, 40, 40)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)

hero1.siapa()
hero1.healthup(5)
hero1.healthup(10)
hero2.healthup(1)

print(hero1.getHealth())
print(hero2.getHealth())




