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
            first = genotype.description[i]
            first_neg = False
            if first < 0:
                first_neg = True
                first = abs(first)
            first -= 1

            second = genotype.description[i+1]
            second_neg = False
            if second < 0:
                second_neg = True
                second = abs(second)
            second -= 1

            third = genotype.description[i+2]
            third_neg = False
            if third < 0:
                third_neg = True
                third = abs(third)
            third -= 1

            first_var = True if genotype.assignment[first] == 'T' else False
            if first_neg:
                first_var = not first_var

            second_var = True if genotype.assignment[second] == 'T' else False
            if second_neg:
                second_var = not second_var

            third_var = True if genotype.assignment[third] == 'T' else False
            if third_neg:
                third_var = not third_var

            clause_val = first_var or second_var or third_var

            if clause_val:
                true_clauses += 1

        print "DD {0}, {1}, {2}".format(true_clauses, 0, 0)
        return true_clauses
