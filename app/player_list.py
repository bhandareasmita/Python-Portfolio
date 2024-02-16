from player_node import PlayerNode
from player import Player


class PlayerList:
    def __init__(self):
        self._head = None
        self._tail = None

    def get_head(self):
        return self._head

    def get_tail(self):
        return self._tail

    def is_empty(self):
        if self._head is None:
            return True
        return False

    def push(self, player_id, player_name):
        new_player = PlayerNode(Player(player_id, player_name))
        if self.is_empty():
            self._head = new_player
            self._tail = self._head
        else:
            new_player.next = self._head
            new_player.prev = None
            self._head = new_player


