from __future__ import annotations
# from typing import TYPE_CHECKING
from player import Player


class PlayerNode:
    def __init__(self, player: Player):
        self._player = player
        self.next = None
        self.prev = None

    @property
    def player(self) -> Player:
        return self._player

    @property
    def key(self):
        return self._player.uid

    def __str__(self):
        return f"{self.player.uid} : {self.player.name}"

