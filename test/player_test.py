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
        self.assertEqual(dl_list._tail.key, '34')
        self.assertIsNone(dl_list._head.next)

    def test_for_adding_new_player_when_list_contains(self):
        dl_list = PlayerList()
        dl_list.push('14', 'Ron')
        dl_list.push('56', 'Ann')
        self.assertIsNotNone(dl_list._head)
        self.assertIsNotNone(dl_list.is_empty())
        self.assertEqual(dl_list._head.key, '56')
        self.assertEqual(dl_list._tail.key, '14')

    def test_for_head_and_tail_when_list_empty(self):
        dl_list = PlayerList()
        self.assertIsNone(dl_list._head)
        self.assertIsNone(dl_list._tail)

    def test_for_head_and_tail_when_list_contains_one_element(self):
        dl_list = PlayerList()
        dl_list.push('23', 'Josh')
        self.assertEqual(dl_list._head.player.name, 'Josh')
        self.assertEqual(dl_list._tail.player.name, 'Josh')
        self.assertIsNotNone(dl_list.is_empty())


if __name__ == '__main__':
    unittest.main()

