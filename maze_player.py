import pygame

from tile import TILE_SIZE, Tile
from direction import Direction
from maze import Maze

WAIT_TIME_MS = 100

# maybe maze should be a global, idk
# cuz there's only ever one of it during a simulation
# same one is reused every route evaluation


def setup_graphics(window_w, window_h):
    global WINDOW_WIDTH, WINDOW_HEIGHT
    WINDOW_WIDTH = window_w
    WINDOW_HEIGHT = window_h

    global SCREEN
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.display.set_caption('Genetic algorithm thing')


def draw_maze(maze: Maze):
    for x in range(0, WINDOW_WIDTH, TILE_SIZE):
        for y in range(0, WINDOW_HEIGHT, TILE_SIZE):
            row, col = int(y / TILE_SIZE), int(x / TILE_SIZE)
            rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(SCREEN, maze.get_tile(row, col).color, rect)


class MazePlayer:
    def __init__(self, row, col, maze: Maze):
        self.row = row
        self.col = col
        self.maze = maze

        self._update_maze()

    def move(self, direction: Direction):
        row = self.row + direction.vec[0]
        col = self.col + direction.vec[1]
        if not self.maze.is_valid_dest(row, col):
            return
        self.row = row
        self.col = col

        self._update_maze()

    def _update_maze(self):
        draw_maze(self.maze)
        # TODO: fix inaccurate player starting position
        # draw player
        x = self.col * TILE_SIZE
        y = self.row * TILE_SIZE
        player_rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(SCREEN, Tile.PLAYER.color, player_rect)
        pygame.display.update()
        pygame.time.wait(WAIT_TIME_MS)
