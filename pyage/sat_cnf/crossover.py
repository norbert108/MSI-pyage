__author__ = 'norbert'
from pyage.solutions.evolution.crossover import AbstractCrossover
from genotype import CNF

class CNFCrossover(AbstractCrossover):
    def __init__(self, size=5):
        super(CNFCrossover, self).__init__(CNF, size)
        self.size = size

    def cross(self, p1, p2):
        # TODO do it more like crossing...
        crossed_assignment = p1.assignment[:len(p1.assignment)/2] + p2.assignment[len(p1.assignment)/2:]
        genotype = CNF(p1.description, crossed_assignment)

        return genotype

