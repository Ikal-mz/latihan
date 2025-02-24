class Hero:

    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("{} dengan health {}".format(self.name,self.health))

class Hero_tank(Hero):
    def __init__(self, name):
        # Hero.__init__(self,name,100)
        super().__init__(name, 100)
        super().showInfo()

class Hero_mage(Hero):
    def __init__(self, name):
        super().__init__(name, 50)
        super().showInfo()

lolita = Hero_tank('lolita')
nana = Hero_mage('nana')