import pygame
import sys

from genetic_alg import GeneticAlg
from maze import Maze

MAZE_FILEPATH = "mazes/m1.txt"

# Genetic Algorithm Parameters
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.001
POPULATION_SIZE = 10
CHROMOSOME_LENGTH = 60


def file_to_array(file):
    maze_array = []
    with open(file, "r") as f:
        for line in f.readlines():
            maze_array.append([int(c) for c in line.rstrip()])
    return maze_array


def main():
    # populate grid w/ correct layout from maze file
    maze_array = file_to_array(MAZE_FILEPATH)
    maze = Maze(maze_array, 1, 14, 1, 0)

    ga = GeneticAlg(CROSSOVER_RATE, MUTATION_RATE, POPULATION_SIZE, CHROMOSOME_LENGTH, maze)

    # TODO: Add ui to display current generation, genome, fitness, etc.
    # could also add in a thing to condense the routes (remove useless movements)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        ga.epoch()
        pygame.display.update()
        if ga.fittest_genome.fitness >= 0.5:
            g = ga.fittest_genome
            print('\nSOLUTION FOUND')
            print('Chromosome: {0}\nFitness: {1}'.format(g.chromosome, g.fitness))
            break


if __name__ == "__main__":
    main()
