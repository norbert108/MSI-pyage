from pyage.core.operator import Operator
from genotype import CNF

import logging
logger = logging.getLogger(__name__)


class CNFEvaluation(Operator):
    def __init__(self):
        super(CNFEvaluation, self).__init__(CNF)

    def process(self, population):
        for genotype in population:
            genotype.fitness = self.evaluate(genotype)

    def evaluate(self, genotype):
        true_clauses = 0
        for i in range(0, len(genotype.description), 3):
            first = int(genotype.description[i]) - 1
            second = int(genotype.description[i+1]) - 1
            third = int(genotype.description[i+2]) - 1

            clause_val = (True if genotype.assignment[first] == 'T' else False) or\
                         (True if genotype.assignment[second] == 'T' else False) or\
                         (True if genotype.assignment[third] == 'T' else False)

            if clause_val:
                true_clauses += 1

        return true_clauses
