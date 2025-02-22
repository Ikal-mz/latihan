class Hero:

    # class variable
    jumlah = 0
    __privateJumlah = 0

    def __init__(self,name,health):
        self.name = name
        self.health = health

        # variable instance private
        self.__private = "private"
        
        # variable instance protected
        self._protected = 'protected'

ona = Hero("Ona", 100)

print(ona.__dict__)
print('\n')
print(Hero.__dict__)