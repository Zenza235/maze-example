import random


class Genome:
    def __init__(self, num_bits=0):
        self.fitness = 0
        self._num_bits = num_bits
        temp_num = random.getrandbits(num_bits)
        self.chromosome = f'{temp_num:0{self._num_bits}b}'

    def __repr__(self):
        return '({0}, {1})'.format(self.chromosome, self.fitness)

    def __eq__(self, other):
        return self.chromosome == other.chromosome
