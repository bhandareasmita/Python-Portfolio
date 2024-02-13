import unittest
from player import Player

class PlayerTest(unittest.TestCase):
    def test_for_uid(self):
        player = Player('11', 'Amy')
        self.assertEqual('11', player.uid)

    def test_for_name(self):
        player = Player('12', 'John')
        self.assertEqual('John', player.name)


if __name__ == '__main__':
    unittest.main()

