class Character:
    def __init__(s,health,damage,speed): 
        #Whenever we assign a class to a variable, the __init__ method is executed by default, irrespective of whether we define it or not.
        #s is the variable to which we will assign the class Character; we often write "Self" in place of "s"
        s.health=health
        s.damage=damage
        s.speed=speed
    def boost(s):
        s.health=1.2*(s.health)
        s.damage=1.5*(s.damage)
        s.speed=2*(s.speed)
        print(s.health)
Assassin=Character(90,30,80) #s=Assassin
Warrior=Character(100,60,40) #s=Warrior
print(Assassin.speed)
Character.boost(Assassin)
print(Character.boost(Assassin)) 
#line 17 prints 129.6(Assassin's Boosted-Boosted Health) and then prints "None" because definition boost(s) does not return anything in the end. 