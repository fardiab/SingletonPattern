class chemistry:
    __instance = None
    @staticmethod
    def getInstance():
        if chemistry.__instance == None:
            chemistry()
        return chemistry.__instance
    def __init__(self):
        if chemistry.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            chemistry.__instance = self