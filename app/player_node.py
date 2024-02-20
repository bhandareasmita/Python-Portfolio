from __future__ import annotations
# from typing import TYPE_CHECKING
from player import Player


class PlayerNode:
    """
    Represents a player node
    """

    def __init__(self, player: Player):
        """
        Initializes a new instance of the PlayerNode class
        Args:
            player: Player object
        """
        self._player = player
        self.next = None
        self.prev = None

    @property
    def player(self) -> Player:
        """
        Get the Player object
        Returns:
            Player object
        """
        return self._player

    @property
    def key(self):
        """
        Get the unique identifier of the player
        Returns:
            int: Unique identifier of the player
        """
        return self._player.uid

    def __str__(self):
        """
        Returns the string representation of the node
        Returns:
            str: String representation of the node
        """
        return f"{self.player.uid} : {self.player.name}"

