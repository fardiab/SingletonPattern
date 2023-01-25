class hero:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(hero, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp

    def show(self):
        print(self.name, self.hp, self.mp)

h1 = hero('Radud', 100, 100)