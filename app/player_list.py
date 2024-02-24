from player_node import PlayerNode
from player import Player
from prettytable import PrettyTable


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

    @property
    def head(self):
        """
        Get the head of the player list
        Returns:
            The head of the player list
        """
        return self._head

    @head.setter
    def head(self, node):
        """
        Set the head of the player list to the specified node
        Args:
            node: The node to set as the head of the player list
        Returns:
            None
        """
        self._head = node

    @property
    def tail(self):
        """
        Get the tail of the player list
        Returns:
            The tail of the player list
        """
        return self._tail

    @tail.setter
    def tail(self, node: PlayerNode):
        """
        Set the tail of the player list to the specified node
        Args:
            node: The node to set as the head of the player list
        Returns:
            None
        """
        self._tail = node

    def is_empty(self) -> bool:
        """
        Check if the player list is empty

        Returns:
            True if the player list is empty, False otherwise
        """
        return self.head is None

    def push(self, player_id: str, player_name: str) -> None:
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
            self.head = new_player
            self.tail = new_player
        else:
            new_player.next = self.head
            self.head.prev = new_player
            self.head = new_player
            new_player.prev = None
        print(f'{new_player} is added to the player list')

    def insert_at_the_tail(self, player_id: str, player_name: str) -> None:
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
            self.head = new_player
            self.tail = new_player
        else:
            last_node = self.tail
            new_player.prev = last_node
            last_node.next = new_player
            new_player.next = None
            self.tail = new_player
        print(f'{new_player} is added to the player list')

    def delete_from_the_head(self) -> str:
        """
        Delete the player from the head of the player list

        Returns:
            str: Name of the removed player
        """
        if self.is_empty():
            return "List is empty"
        else:
            popped_node = self.head
            self.head = popped_node.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None

        print(f'{popped_node} is removed from the player list')
        return popped_node.player.name

    def delete_from_the_tail(self) -> str:
        """
        Delete the player from the tail of the player list

        Returns:
            str: Name of the removed player
        """
        if self.is_empty():
            return "List is empty"
        else:
            popped_node = self.tail
            self.tail = popped_node.prev
            if self.tail is not None:
                self.tail.next = None
            else:
                self.head = None
        print(f'{popped_node} is removed from the player list')
        return popped_node.player.name

    def delete_by_key(self, player_id: str) -> str | None:
        """
        Delete the player with specified id from the player list
        Args:
            player_id (int): Unique id of the player

        Returns:
            str: Indicating whether the player was found and deleted or not
        """
        current_player = self.head
        while current_player is not None:
            if current_player.key == player_id:
                if current_player.prev is None:
                    self.head = current_player.next
                else:
                    current_player.prev.next = current_player.next
                    if current_player.next is not None:
                        current_player.next.prev = current_player.prev
                print(f'{current_player} is removed from the player list')
                return 'Player removed from the list'
            current_player = current_player.next
        print('Invalid player ID provided')
        return 'Player not found'

    def display_player_list(self, forward=True) -> PrettyTable:
        """
        Display the player list in a forward or a reverse direction
        Args:
            forward (bool): Include forward or reverse direction, defaults to True

        Returns:
            PrettyTable: Table of the player list
        """
        forward_table = PrettyTable(['Player ID', 'Player Name'])
        forward_table.title = " FORWARD Player List"
        backward_table = PrettyTable(['Player ID', 'Player Name'])
        backward_table.title = " BACKWARD Player List"
        if forward:
            current_node = self.head
            while current_node:
                forward_table.add_row([current_node.key, current_node.player.name])
                current_node = current_node.next
            return forward_table

        else:
            current_node = self.tail
            while current_node:
                backward_table.add_row([current_node.key, current_node.player.name])
                current_node = current_node.prev
            return backward_table

