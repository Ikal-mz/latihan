class Hero:

    def __init__(self,name,health,armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.info = "name {} : \n\t".format(self.name,self.__health)

    @property
    def info(self):
        return "name {} : \n\thealth {}".format(self.name,self.__health)

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self,input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print('armor di delete')
        self.__armor = None

zilong = Hero('zilong',80,60)
print('merubah info')
print(zilong.info)
zilong.name = 'dadang'
print(zilong.info)

print('getter dan setter untuk __armor:')
print(zilong.armor)
zilong.armor = 100
print(zilong.armor)

print('delete armor')
del zilong.armor
print(zilong.__dict__)

    
