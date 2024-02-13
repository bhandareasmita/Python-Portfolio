class Player:
    def __init__(self, uid, name):
        self._uid = uid
        self._name = name

    @property
    def uid(self):
        return self._uid

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f'Name: {self._name}\nId: {self._uid}'

