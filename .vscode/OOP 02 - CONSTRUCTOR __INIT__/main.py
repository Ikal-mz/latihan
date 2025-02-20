class Hero: # template
    def __init__(self,inputName,inputHealth,inputPower,inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor


hero1 = Hero("Miya", 60, 80, 20)
hero2 = Hero("Lukas", 70, 70, 30)
hero3 = Hero("Lolita", 80, 40, 40)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)

