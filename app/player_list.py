from player_node import PlayerNode
from player import Player


class PlayerList:
    def __init__(self):
        self._head = None
        self._tail = None

    def get_head(self):
        return self._head

    def set_head(self, node):
        self._head = node

    def get_tail(self):
        return self._tail

    def set_tail(self, node):
        self._tail = node

    def is_empty(self):
        if self.get_head() is None:
            return True
        return False

    def push(self, player_id, player_name):
        new_player = PlayerNode(Player(player_id, player_name))
        if self.is_empty():
            self.set_head(new_player)
            self.set_tail(new_player)
        else:
            new_player.next = self.get_head()
            self.get_head().prev = new_player
            self.set_head(new_player)
            new_player.prev = None

    def insert_at_the_tail(self, player_id, player_name):
        new_player = PlayerNode(Player(player_id, player_name))
        if self.is_empty():
            self.set_head(new_player)
            self.set_tail(new_player)
        else:
            last_node = self.get_tail()
            new_player.prev = last_node
            last_node.next = new_player
            new_player.next = None
            self.set_tail(new_player)



