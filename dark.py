class dark:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if dark.__instance == None:
            dark()
        return dark.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if dark.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            dark.__instance = self

    def __str__(self):
        return 'dark'