class Hero:

    def __init__(self,name,health,attackPower,armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def serang(self, lawan):
        print(self.name, 'menyerang', lawan.name)
        lawan.diserang(self, self.attackPower)

    def diserang(self, lawan, attackPower_lawan):
        print(self.name, "diserang", lawan.name)
        attack_diterima = attackPower_lawan/self.armorNumber
        print('serangan terasa : ', str(attack_diterima))
        self.health -= attack_diterima
        print('darah', self.name, ' tersisa', str(self.health))

nana = Hero('nana', 80, 80, 40)
lolita = Hero('lolita', 80, 50, 80)

nana.serang(lolita)
print("\n")
lolita.serang(nana)
print("\n")
lolita.serang(nana)
