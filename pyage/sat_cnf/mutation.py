__author__ = 'norbert'

from pyage.solutions.evolution.mutation import AbstractMutation
from genotype import CNF
import random


class CNFMutation(AbstractMutation):
    def __init__(self, type=None, probability=0.1):
        super(CNFMutation, self).__init__(CNF, probability)

    def mutate(self, genotype):
        random.seed()
        mutated_values = random.randint(0, len(genotype.assignment)-1)

        indices = random.sample(range(len(genotype.assignment)), mutated_values)

        mutated_assignment = list(genotype.assignment)
        for index in indices:
            mutated_assignment[index] = "T" if mutated_assignment[index] == "F" else "F"

        genotype.assignment = mutated_assignment