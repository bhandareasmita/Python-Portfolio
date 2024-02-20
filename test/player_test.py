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
        self.assertEqual(dl_list.get_head().key, '34')
        self.assertEqual(dl_list.get_tail().key, '34')
        self.assertIsNone(dl_list.get_head().next)

    def test_for_adding_new_player_when_list_contains(self):
        dl_list = PlayerList()
        dl_list.push('14', 'Ron')
        dl_list.push('56', 'Ann')
        self.assertIsNotNone(dl_list._head)
        self.assertIsNotNone(dl_list.is_empty())
        self.assertEqual(dl_list.get_head().key, '56')
        self.assertEqual(dl_list.get_tail().key, '14')

    def test_for_head_and_tail_when_list_empty(self):
        dl_list = PlayerList()
        self.assertIsNone(dl_list.get_head())
        self.assertIsNone(dl_list.get_tail())

    def test_for_head_and_tail_when_list_contains_one_element(self):
        dl_list = PlayerList()
        dl_list.push('23', 'Josh')
        self.assertEqual(dl_list.get_head().player.name, 'Josh')
        self.assertEqual(dl_list.get_tail().player.name, 'Josh')
        self.assertIsNotNone(dl_list.is_empty())

    def test_for_insert_at_the_tail_when_list_empty(self):
        dl_list = PlayerList()
        dl_list.insert_at_the_tail('3', 'Sammy')
        self.assertEqual(dl_list.get_head().player.name, 'Sammy')
        self.assertEqual(dl_list.get_tail().player.uid, '3')

    def test_for_insert_at_the_tail_when_list_contains(self):
        dl_list = PlayerList()
        dl_list.push('1', 'Asmita')
        dl_list.push('2', 'Rose')
        dl_list.insert_at_the_tail('3', 'Sammy')
        self.assertEqual(dl_list.get_tail().player.name, 'Sammy')
        self.assertEqual(dl_list.get_tail().prev.player.name, 'Asmita')

    def test_for_delete_from_the_head_when_list_empty(self):
        dl_list = PlayerList()
        self.assertEqual(dl_list.delete_from_the_head(), 'List is empty')

    def test_for_delete_from_the_head_when_list_contains(self):
        dl_list = PlayerList()
        dl_list.push('3', 'Rose')
        dl_list.push('4', 'John')
        self.assertEqual(dl_list.delete_from_the_head(), 'John')
        self.assertEqual(dl_list.get_tail().player.name, 'Rose')
        self.assertEqual(dl_list.get_tail().player.name, 'Rose')

    def test_for_delete_from_the_head_when_list_contains_single_node(self):
        dl_list = PlayerList()
        dl_list.push('3', 'Rose')
        self.assertEqual(dl_list.delete_from_the_head(), 'Rose')
        self.assertEqual(dl_list.is_empty(), True)

    def test_for_delete_from_the_tail_when_list_empty(self):
        dl_list = PlayerList()
        self.assertEqual(dl_list.delete_from_the_tail(), 'List is empty')

    def test_for_delete_from_the_tail_when_list_contains(self):
        dl_list = PlayerList()
        dl_list.push('3', 'Rose')
        dl_list.push('4', 'John')
        self.assertEqual(dl_list.delete_from_the_tail(), 'Rose')
        self.assertEqual(dl_list.get_tail().player.name, 'John')
        self.assertEqual(dl_list.get_tail().player.name, 'John')

    def test_for_delete_from_the_tail_when_list_contains_single_node(self):
        dl_list = PlayerList()
        dl_list.push('3', 'Rose')
        self.assertEqual(dl_list.delete_from_the_tail(), 'Rose')
        self.assertEqual(dl_list.is_empty(), True)

    def test_for_delete_by_key_when_list_empty(self):
        dl_list = PlayerList()
        self.assertEqual(dl_list.delete_by_key('2'), 'Player not found')

    def test_for_delete_by_key_when_list_contains(self):
        dl_list = PlayerList()
        dl_list.push('3', 'Rose')
        self.assertEqual(dl_list.delete_by_key('3'), 'Player removed from the list')


if __name__ == '__main__':
    unittest.main()

