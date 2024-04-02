from tile import Tile


class Maze:
    def get_tile(self, r, c) -> Tile:
        return Tile(self.map[r][c])

    def is_valid_dest(self, r, c) -> bool:
        return (0 <= r < self.height) and (0 <= c < self.width) and self.get_tile(r, c) is not Tile.WALL

    def __init__(self, num_map: list[list[int]], start_row, start_col, end_row, end_col):
        self.map = num_map
        self.width = len(num_map[0])
        self.height = len(num_map)
        self.start_row = start_row
        self.start_col = start_col
        self.end_row = end_row
        self.end_col = end_col
