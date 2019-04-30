class Computer:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def choosePokemon(pkmnList):
        choice = random.randint(1, (len(pkmnList)-1))
