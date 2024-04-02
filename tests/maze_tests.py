import unittest

from maze import Maze


def _file_to_array(file):
    maze_array = []
    with open(file, "r") as f:
        for line in f.readlines():
            maze_array.append([int(c) for c in line.rstrip()])
    return maze_array


class MyTestCase(unittest.TestCase):
    def test_is_valid_dest(self):
        maze_array = _file_to_array("../mazes/baby_maze.txt")
        # num_rows = 2
        # num_cols = 2
        m1 = Maze(maze_array, 7, 14, 2, 0)

        # Out of bounds
        self.assertEqual(False, m1.is_valid_dest(-1, -1))
        # In bounds, tile is a wall
        self.assertEqual(False, m1.is_valid_dest(0, 1))
        # In bounds, tile is NOT a wall (i.e. valid)
        self.assertEqual(True, m1.is_valid_dest(0, 0))


if __name__ == '__main__':
    unittest.main()
