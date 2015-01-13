__author__ = 'norbert'

from pyage.core.operator import Operator
from genotype import CNF
import random


class CNFInitializer(Operator):
    def __init__(self, description, variables):
        super(CNFInitializer, self).__init__(CNF)
        self.description = description
        self.variables = variables

    def process(self, population):
        assignment = []
        for i in range(self.variables):
            assignment.append("T" if random.uniform < 0.5 else "F")

        population.append(CNF(description=self.description, assignment="".join(assignment)))