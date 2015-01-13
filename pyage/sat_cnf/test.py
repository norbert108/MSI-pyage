__author__ = 'norbert'

from evaluation import CNFEvaluation
from genotype import CNF
from crossover import CNFCrossover
from mutation import CNFMutation

from initializer import CNFInitializer

class Genotype:
    def __init__(self, description, assignment):
        self.description = description
        self.assignment = assignment


test_genotype = Genotype("123222", "TFF")
test_genotype2 = Genotype("123222", "TTT")

# eval = CNFEvaluation()
# cross = CNFCrossover()
# crossed = cross.cross(test_genotype, test_genotype2)
#
# mutant = CNFMutation()
# mutated = mutant.mutate(test_genotype)

inited = CNFInitializer("123122", 3)


# print "{0}".format(mutated)