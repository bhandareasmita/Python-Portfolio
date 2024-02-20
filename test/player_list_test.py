import unittest
from player_list import PlayerList
from prettytable import PrettyTable


class PlayerListTest(unittest.TestCase):
    def test_add_new_player_when_list_empty(self):
        dl_list = PlayerList()
        dl_list.push('34', 'Tom')
        self.assertEqual(dl_list.head.key, '34')
        self.assertEqual(dl_list.tail.key, '34')
        self.assertIsNone(dl_list.head.next)

    def test_add_new_player_when_list_contains(self):
        dl_list = PlayerList()
        dl_list.push('14', 'Ron')
        dl_list.push('56', 'Ann')
        self.assertIsNotNone(dl_list._head)
        self.assertIsNotNone(dl_list.is_empty())
        self.assertEqual(dl_list.head.key, '56')
        self.assertEqual(dl_list.tail.key, '14')

    def test_head_and_tail_when_list_empty(self):
        dl_list = PlayerList()
        self.assertIsNone(dl_list.head)
        self.assertIsNone(dl_list.tail)

    def test_head_and_tail_when_list_contains_one_element(self):
        dl_list = PlayerList()
        dl_list.push('23', 'Josh')
        self.assertEqual(dl_list.head.player.name, 'Josh')
        self.assertEqual(dl_list.tail.player.name, 'Josh')
        self.assertIsNotNone(dl_list.is_empty())

    def test_insert_at_the_tail_when_list_empty(self):
        dl_list = PlayerList()
        dl_list.insert_at_the_tail('3', 'Sammy')
        self.assertEqual(dl_list.head.player.name, 'Sammy')
        self.assertEqual(dl_list.tail.player.uid, '3')

    def test_insert_at_the_tail_when_list_contains(self):
        dl_list = PlayerList()
        dl_list.push('1', 'Asmita')
        dl_list.push('2', 'Rose')
        dl_list.insert_at_the_tail('3', 'Sammy')
        self.assertEqual(dl_list.tail.player.name, 'Sammy')
        self.assertEqual(dl_list.tail.prev.player.name, 'Asmita')

    def test_delete_from_the_head_when_list_empty(self):
        dl_list = PlayerList()
        self.assertEqual(dl_list.delete_from_the_head(), 'List is empty')

    def test_delete_from_the_head_when_list_contains(self):
        dl_list = PlayerList()
        dl_list.push('3', 'Rose')
        dl_list.push('4', 'John')
        self.assertEqual(dl_list.delete_from_the_head(), 'John')
        self.assertEqual(dl_list.tail.player.name, 'Rose')
        self.assertEqual(dl_list.tail.player.name, 'Rose')

    def test_delete_from_the_head_when_list_contains_single_node(self):
        dl_list = PlayerList()
        dl_list.push('3', 'Rose')
        self.assertEqual(dl_list.delete_from_the_head(), 'Rose')
        self.assertEqual(dl_list.is_empty(), True)

    def test_delete_from_the_tail_when_list_empty(self):
        dl_list = PlayerList()
        self.assertEqual(dl_list.delete_from_the_tail(), 'List is empty')

    def test_delete_from_the_tail_when_list_contains(self):
        dl_list = PlayerList()
        dl_list.push('3', 'Rose')
        dl_list.push('4', 'John')
        self.assertEqual(dl_list.delete_from_the_tail(), 'Rose')
        self.assertEqual(dl_list.tail.player.name, 'John')
        self.assertEqual(dl_list.tail.player.name, 'John')

    def test_delete_from_the_tail_when_list_contains_single_node(self):
        dl_list = PlayerList()
        dl_list.push('3', 'Rose')
        self.assertEqual(dl_list.delete_from_the_tail(), 'Rose')
        self.assertEqual(dl_list.is_empty(), True)

    def test_delete_by_key_when_list_empty(self):
        dl_list = PlayerList()
        self.assertEqual(dl_list.delete_by_key('2'), 'Player not found')

    def test_delete_by_key_when_list_contains(self):
        dl_list = PlayerList()
        dl_list.push('3', 'Rose')
        self.assertEqual(dl_list.delete_by_key('3'), 'Player removed from the list')

    def test_display_player_list_forward(self):
        expected_forward_table = PrettyTable(['Player ID', 'Player Name'])
        expected_forward_table.title = " FORWARD Player List"
        expected_forward_table.add_row(["4", "D"])
        expected_forward_table.add_row(["3", "C"])
        expected_forward_table.add_row(["2", "B"])
        expected_forward_table.add_row(["1", "A"])
        dl_list = PlayerList()
        dl_list.push('1', 'A')
        dl_list.push('2', 'B')
        dl_list.push('3', 'C')
        dl_list.push('4', 'D')
        self.assertEqual(str(expected_forward_table), str(dl_list.display_player_list(forward=True)))

    def test_display_player_list_backward(self):
        expected_backward_table = PrettyTable(['Player ID', 'Player Name'])
        expected_backward_table.title = " BACKWARD Player List"
        expected_backward_table.add_row(["1", "A"])
        expected_backward_table.add_row(["2", "B"])
        expected_backward_table.add_row(["3", "C"])
        expected_backward_table.add_row(["4", "D"])
        dl_list = PlayerList()
        dl_list.push('1', 'A')
        dl_list.push('2', 'B')
        dl_list.push('3', 'C')
        dl_list.push('4', 'D')
        self.assertEqual(str(expected_backward_table), str(dl_list.display_player_list(forward=False)))


if __name__ == '__main__':
    unittest.main()
