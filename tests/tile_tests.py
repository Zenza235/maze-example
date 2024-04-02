import unittest

from tile import Tile


class MyTestCase(unittest.TestCase):
    def test_maze_array_creation(self):
        filepath = "../mazes/baby_maze.txt"
        maze_array = []
        with open(filepath, "r") as f:
            for line in f.readlines():
                maze_array.append([Tile(int(c)) for c in line.rstrip()])
        expected = [
            [Tile.EMPTY, Tile.WALL],
            [Tile.END, Tile.START]
        ]
        self.assertEqual(expected, maze_array)


if __name__ == '__main__':
    unittest.main()
