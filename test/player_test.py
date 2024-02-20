import unittest
from player import Player


class PlayerTest(unittest.TestCase):
    def test_uid_set_and_can_be_retrieved(self):
        player = Player('11', 'Amy')
        self.assertEqual('11', player.uid)

    def test_name_set_and_can_be_retrieved(self):
        player = Player('12', 'John')
        self.assertEqual('John', player.name)


if __name__ == '__main__':
    unittest.main()

