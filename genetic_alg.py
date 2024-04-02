import numpy as np
import random

from direction import Direction
from genome import Genome
from maze import Maze
from maze_player import MazePlayer, setup_graphics, draw_maze
from tile import TILE_SIZE


def _decode(chromosome):
    return [Direction(int(chromosome[i:i + 2], 2)) for i in range(0, len(chromosome) - 1, 2)]


class GeneticAlg:
    def __init__(self, cross_rate, mut_rate, pop_size, chromo_len, maze: Maze):
        self._cross_rate = cross_rate
        self._mut_rate = mut_rate
        self._pop_size = pop_size
        self._chromo_len = chromo_len
        self._maze = maze

        self._genomes: list[Genome] = []
        self._is_busy = False
        self._fittest_genome = Genome()
        self._best_fitness_score = 0
        self._total_fitness_score = 0
        self._generation = 0

        self._create_start_population()
        setup_graphics(maze.width * TILE_SIZE, maze.height * TILE_SIZE)
        draw_maze(maze)

    @property
    def generation(self):
        return self._generation

    @property
    def fittest_genome(self) -> Genome:
        return self._fittest_genome

    def stop(self):
        self._is_busy = False

    def _mutate(self, g: Genome):
        chromo_list = list(g.chromosome)
        for i, b in enumerate(chromo_list):
            if random.random() < self._mut_rate:
                chromo_list[i] = '0' if b == '1' else '1'

        g.chromosome = ''.join(chromo_list)

    def _crossover(self, p1: Genome, p2: Genome, c1: Genome, c2: Genome):
        if (random.random() > self._cross_rate) or (p1 == p2):
            c1.chromosome = p1.chromosome
            c2.chromosome = p2.chromosome
            return

        cross_point = random.randint(0, self._chromo_len - 1)
        c1.chromosome = p1.chromosome[0:cross_point] + p2.chromosome[cross_point::]
        c2.chromosome = p2.chromosome[0:cross_point] + p1.chromosome[cross_point::]

    def _roulette_selection(self):
        rand_slice = random.random() * self._total_fitness_score
        cum_fitness = 0
        selected_genome = 0
        for i in range(0, self._pop_size):
            cum_fitness += self._genomes[i].fitness
            if cum_fitness > rand_slice:
                selected_genome = i
                break
        return self._genomes[selected_genome]

    def _eval_route(self, route):
        player = MazePlayer(self._maze.start_row, self._maze.start_col, self._maze)
        for direction in route:
            player.move(direction)


        diff_x = abs(player.row - self._maze.end_row)
        diff_y = abs(player.col - self._maze.end_col)

        # calculated fitness
        return 1 / (diff_x + diff_y + 1)

    def _update_fitness_scores(self):
        pop_fitness = []
        for g in self._genomes:
            g_route = _decode(g.chromosome)
            g.fitness = self._eval_route(g_route)
            print(g)

            pop_fitness.append(g.fitness)

        pop_fitness = np.array(pop_fitness)
        self._fittest_genome = self._genomes[pop_fitness.argmax()]
        self._total_fitness_score = pop_fitness.sum()

    def _create_start_population(self):
        for i in range(0, self._pop_size):
            self._genomes.append(Genome(self._chromo_len))

    def epoch(self):
        print('\nGeneration: {0}'.format(self.generation))
        print('Fittest Genome: {0}'.format(self.fittest_genome))
        self._update_fitness_scores()

        # create new population
        new_population = []
        num_babies = 0
        while num_babies < self._pop_size:
            p1 = self._roulette_selection()
            p2 = self._roulette_selection()
            c1 = Genome()
            c2 = Genome()
            self._crossover(p1, p2, c1, c2)
            self._mutate(c1)
            self._mutate(c2)
            new_population.append(c1)
            new_population.append(c2)
            num_babies += 2
        self._genomes = new_population
        self._generation += 1
