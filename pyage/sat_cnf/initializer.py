__author__ = 'norbert'

from pyage.core.operator import Operator
from genotype import CNF
from pyage.core.emas import EmasAgent
import random


class CNFInitializer(Operator):
    def __init__(self, description, variables, size=100):
        super(CNFInitializer, self).__init__(CNF)
        self.description = description
        self.variables = variables
        self.size = size

    def process(self, population):
        for genotype_no in range(self.size):
            assignment = []
            for i in range(self.variables):
                assignment.append("T" if random.uniform(0, 1) < 0.5 else "F")

            population.append(CNF(description=self.description, assignment=assignment))


def cnf_emas_initializer(description, variables, energy=10, size=100):
    agents = {}
    for i in range(size):
        assignment = []
        for j in range(variables):
            assignment.append("T" if random.uniform(0, 1) < 0.5 else "F")

        agent = EmasAgent(CNF(description, assignment), energy)
        agents[agent.get_address()] = agent
    return agents