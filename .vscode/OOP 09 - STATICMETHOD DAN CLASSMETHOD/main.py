class Hero:

    # privet class variable
    __jumlah = 0

    def __init__(self,name):
        self.__name = name
        Hero.__jumlah += 1

    # method ini hanya berlaku untuk object
    def getJumlah(self):
        return Hero.__jumlah
    
    # method ini tidak berlaku untuk object, tapi berlaku untuk class
    def getJumlah1():
        return Hero.__jumlah
    
    # method static (decorator) nempel ke object dan class
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah
    
    @classmethod
    def getJumlah3(cls):
        return Hero.__jumlah




zilong = Hero('zilong')
print(zilong.getJumlah())
print(Hero.getJumlah1())
badang = Hero('badang')
print(Hero.getJumlah2())
saber = Hero('saber')
print(Hero.getJumlah3())
