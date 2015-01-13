__author__ = 'norbert'

from pyage.solutions.evolution.mutation import AbstractMutation
from genotype import CNF
import random


class CNFMutation(AbstractMutation):
    def __init__(self, type=None, probability=0.01):
        super(CNFMutation, self).__init__(CNF, probability)

    def mutate(self, genotype):
        random.seed()
        mutated_values = random.randint(0, len(genotype.assignment))
        print "SAMPEL {0}".format(mutated_values)

        # indices = random.sample(range(len(genotype.assignment)), mutated_values)
        indices = [0, 1]

        mutated_assignment = list(genotype.assignment)
        for index in indices:
            mutated_assignment[index] = "T" if genotype.assignment[index] == "F" else "T"

        genotype.assignment = mutated_assignment
        return genotype.assignment