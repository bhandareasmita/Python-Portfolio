from player_node import PlayerNode
from player import Player


class PlayerList:
    """
    This class is responsible for creating a player list
    """
    def __init__(self):
        """
        Initializes the player list
        """
        self._head = None
        self._tail = None

    def get_head(self):
        """
        Get the head of the player list
        Returns:
            The head of the player list
        """
        return self._head

    def set_head(self, node):
        """
        Set the head of the player list to the specified node
        Args:
            node: The node to set as the head of the player list
        Returns:
            None
        """
        self._head = node

    def get_tail(self):
        """
        Get the tail of the player list
        Returns:
            The tail of the player list
        """
        return self._tail

    def set_tail(self, node):
        """
        Set the tail of the player list to the specified node
        Args:
            node: The node to set as the head of the player list
        Returns:
            None
        """
        self._tail = node

    def is_empty(self):
        """
        Check if the player list is empty

        Returns:
            True if the player list is empty, False otherwise
        """
        if self.get_head() is None:
            return True
        return False

    def push(self, player_id, player_name):
        """
        Add a player to the player list
        Args:
            player_id: Unique id of the player
            player_name: Name of the player

        Returns:
            None
        """
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
        """
        Add a player to the tail of the player list
        Args:
            player_id: Unique id of the player
            player_name: Name of the player

        Returns:
            None
        """
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

    def delete_from_the_head(self):
        """
        Delete the player from the head of the player list
        Returns:
            None
        """
        if self.is_empty():
            return "List is empty"
        else:
            popped_node = self._head
            self._head = popped_node.next
            if self._head is not None:
                self._head.prev = None
            else:
                self._tail = None
        return popped_node.player.name

    def delete_from_the_tail(self):
        """
        Delete the player from the tail of the player list
        Returns:
            None
        """
        if self.is_empty():
            return "List is empty"
        else:
            popped_node = self._tail
            self._tail = popped_node.prev
            if self._tail is not None:
                self._tail.next = None
            else:
                self._head = None
        return popped_node.player.name



