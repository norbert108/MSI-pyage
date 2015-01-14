__author__ = 'norbert'

from evaluation import CNFEvaluation
from genotype import CNF
from crossover import CNFCrossover
from mutation import CNFMutation
import random

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

random.seed()

variables = 10
clauses = 100
sat_lst = []

for i in range(clauses):
    for j in range(3):
        rnd = random.randint(1, variables)
        if random.uniform(0, 1) > 0.3:
            rnd = -rnd
        sat_lst.append(rnd)

# print sat_lst

indices = random.sample(range(len([1,2,3,4,5,6,7,8,9,0,11,12,13,14])), 5)
print indices