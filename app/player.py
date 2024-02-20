class Player:
    """
    Represents a player in a game
    """
    def __init__(self, uid: int, name: str):
        """
        Initializes a new Player object
        Args:
            uid (int): The unique identifier for the player.
            name (str): The name of the player.
        """
        self._uid = uid
        self._name = name

    @property
    def uid(self) -> int:
        """
        Gets the unique identifier of the player
        Returns:
            int: The unique identifier of the player.
        """
        return self._uid

    @property
    def name(self) -> str:
        """
        Gets the name of the player
        Returns:
            str: The name of the player
        """
        return self._name

    def __str__(self) -> str:
        """
        Returns a string representation of the player
        Returns:
            str: A string representation of the player
        """
        return f'Name: {self._name}\nId: {self._uid}'

