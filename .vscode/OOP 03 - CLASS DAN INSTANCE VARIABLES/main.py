class Hero: # template
    # class variable
    jumlah = 0

    def __init__(self,inputName,inputHealth,inputPower,inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print("Nama Hero : " , inputName)


hero1 = Hero("Miya", 60, 80, 20)
print(Hero.jumlah)
hero2 = Hero("Lukas", 70, 70, 30)
print(Hero.jumlah)
hero3 = Hero("Lolita", 80, 40, 40)
print(Hero.jumlah)



