class Player:
    def __init__(self, uid, name):
        self.__uid = uid
        self.__name = name

    @property
    def uid(self):
        return self.__uid

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f'Name: {self.__name}\nId: {self.__uid}'


p = Player('11', 'Amy')
print(p)