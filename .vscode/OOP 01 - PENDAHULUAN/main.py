class Hero: # template
    pass


hero1 = Hero() # object / instance(instansiate)
hero2 = Hero()
hero3 = Hero()

hero1.name = "Lukas"
hero1.health =80

hero2.name = "Miya"
hero2.health = 60

hero3.name = "Lolita"
hero3.health = 97

print(hero1)
print(hero1.__dict__)
print(hero1.name)
