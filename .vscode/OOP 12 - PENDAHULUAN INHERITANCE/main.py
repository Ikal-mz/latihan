class Hero:

    def __init__(self,name,health):
        self.name = name
        self.health = health

class Hero_tank(Hero):
    pass

class Hero_mage(Hero):
    pass

estes = Hero('estes', 90)
lolita = Hero_tank('lolita',100)
nana = Hero_mage('nana',70)

print(estes.name)
print(lolita.name)
print(help(nana))