class Hero:

    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showInfo(self):
        print('showinfo di class Hero')
        print("{} \n\tdengan health {}".format(self.name,self.health))

class Hero_tank(Hero):
    def __init__(self, name):
        # Hero.__init__(self,name,100)
        super().__init__(name, 100)

    # override
    def showInfo(self):
        print('showinfo di subclass Hero_tank')
        print("{} \n\ttipe : tank dengan health {}".format(
            self.name,
            self.health
            )
        )


class Hero_mage(Hero):
    def __init__(self, name):
        super().__init__(name, 50)
        

lolita = Hero_tank('lolita')
nana = Hero_mage('nana')

lolita.showInfo()
nana.showInfo()