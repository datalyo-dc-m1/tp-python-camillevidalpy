class Monkey:
    def __init__(self, name):
        self.name = name

    def eat(self, banana):
        print(self.name, 'a mangé une banane', banana.color)


class Banana:
    def __init__(self, color):
        self.color = color


banana_green = Banana('verte')
banana_yellow = Banana('jaune')
pierre = Monkey("Pierre")
Marie = Monkey("Marie")

pierre.eat(banana_yellow)
Marie.eat(banana_green)

#Correction
class Monkey:

    def __init__(self, name):
        self.name = name

    def mange(self, banane):
        print(self.name, "mange une banane de couleur", banane.couleur)

    def reproduire(self,monkey):
        print(self.name, "et", monkey.name, "reproduisent", Robert.name)
        child = Monkey("Robert")




class Banane:

    def __init__(self, couleur):
        self.couleur = couleur


pierre = Monkey("Pierre")
banane_jaune = Banane("jaune")
Marie = Monkey("Marie")
banane_verte = Banane("Verte")
Robert = Monkey("Robert")

pierre.mange(banane_jaune)
Marie.mange (banane_verte)
pierre.reproduire(Marie)
