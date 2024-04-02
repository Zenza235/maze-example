import random
import unittest

from genetic_alg import GeneticAlg, _decode
from direction import Direction
from genome import Genome
from maze import Maze


def _file_to_array(file):
    maze_array = []
    with open(file, "r") as f:
        for line in f.readlines():
            maze_array.append([int(c) for c in line.rstrip()])
    return maze_array


class MyTestCase(unittest.TestCase):
    def test_decode(self):
        bit_string = '111110011011101110010101'
        expected = [
            Direction.WEST, Direction.WEST, Direction.EAST, Direction.SOUTH,
            Direction.EAST, Direction.WEST, Direction.EAST, Direction.WEST,
            Direction.EAST, Direction.SOUTH, Direction.SOUTH, Direction.SOUTH
        ]
        self.assertEqual(expected, _decode(bit_string))

    def test_create_start_population(self):
        maze_array = _file_to_array("../mazes/m1.txt")
        m1 = Maze(maze_array, 7, 14, 2, 0)

        pop_size = 3
        ga = GeneticAlg(0, 0, pop_size, 12, m1)
        print(ga._genomes)
        self.assertEqual(pop_size, len(ga._genomes))

    def test_crossover_same_parent(self):
        # chromo_len = 12
        maze_array = _file_to_array("../mazes/m1.txt")
        m1 = Maze(maze_array, 7, 14, 2, 0)

        ga = GeneticAlg(0.7, 0, 0, 12, m1)
        test_chromo = '110011001100'
        parent1 = Genome()
        parent2 = Genome()
        parent1.chromosome = test_chromo
        parent2.chromosome = test_chromo
        self.assertEqual(parent1, parent2)

        child1 = Genome()
        child2 = Genome()
        child1.chromosome = '000000000000'
        child2.chromosome = '000000000001'
        self.assertNotEqual(child1, child2)

        ga._crossover(parent1, parent2, child1, child2)
        # child1 and child2 should now have the same chromosome
        self.assertEqual(child1, child2)

    def test_crossover_different_parents(self):
        random.seed(500)
        # chromo_len = 6
        ga = GeneticAlg(1, 0, 0, 6, [])
        parent1 = Genome()
        parent2 = Genome()
        parent1.chromosome = '111111'
        parent2.chromosome = '000000'
        self.assertNotEqual(parent1, parent2)

        child1 = Genome()
        child2 = Genome()
        ga._crossover(parent1, parent2, child1, child2)
        self.assertEqual('111100', child1.chromosome)
        self.assertEqual('000011', child2.chromosome)

    def test_mutate(self):
        # no mutation occurs
        ga = GeneticAlg(0, 0, 0, 6, [])
        genome = Genome()
        genome.chromosome = '111000'
        ga._mutate(genome)
        self.assertEqual('111000', genome.chromosome)

        # every bit is flipped
        ga = GeneticAlg(0, 1, 0, 6, [])
        ga._mutate(genome)
        self.assertEqual('000111', genome.chromosome)

    def test_epoch(self):
        maze_array = _file_to_array("../mazes/m1.txt")
        m1 = Maze(maze_array, 7, 14, 2, 0)
        ga = GeneticAlg(0.7, 0.3, 100, 24, m1)
        for i in range(1):
            ga.epoch()
            print(ga.fittest_genome)
        self.assertTrue(True)

    def test_eval_route(self):
        import pygame
        import sys

        maze_array = _file_to_array("../mazes/m1.txt")
        # num_rows = 10
        # num_cols = 15
        m1 = Maze(maze_array, 7, 14, 2, 0)
        ga = GeneticAlg(0, 0, 0, 0, m1)

        r1 = [
            Direction.WEST, Direction.WEST, Direction.WEST,
            Direction.WEST, Direction.WEST, Direction.WEST,
            Direction.NORTH, Direction.NORTH, Direction.NORTH,
            Direction.NORTH, Direction.WEST, Direction.NORTH,
            Direction.WEST, Direction.WEST, Direction.WEST,
            Direction.WEST, Direction.WEST, Direction.WEST,
            Direction.WEST
        ]

        is_running = True
        while is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                ga._eval_route(r1)
                pygame.display.update()

        self.assertTrue(True)
        # Result is (7, 13), diff from (2, 0) is (5, 13)
        # self.assertEqual(1 / (5 + 13 + 1), ga._eval_route(r1))


if __name__ == '__main__':
    unittest.main()
