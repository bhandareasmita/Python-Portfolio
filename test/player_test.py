import unittest
from player import Player
from player_list import PlayerList


class PlayerTest(unittest.TestCase):
    def test_for_uid(self):
        player = Player('11', 'Amy')
        self.assertEqual('11', player.uid)

    def test_for_name(self):
        player = Player('12', 'John')
        self.assertEqual('John', player.name)

    def test_for_adding_new_player_when_list_empty(self):
        dl_list = PlayerList()
        dl_list.push('34', 'Tom')
        self.assertEqual(dl_list._head.key, '34')
        self.assertIsNone(dl_list._head.next)

    def test_for_adding_new_player_when_list_contains(self):
        dl_list = PlayerList()
        dl_list.push('14', 'Ron')
        dl_list.push('56', 'Ann')
        self.assertIsNotNone(dl_list._head)
        self.assertIsNotNone(dl_list.is_empty())
        self.assertEqual(dl_list._head.key, '56')


if __name__ == '__main__':
    unittest.main()

