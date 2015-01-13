class CNF(object):

    def __init__(self, description, assignment):
        self.assignment = assignment
        self.description = description
        self.fitness = None

    def __str__(self):
        return "{0}\nfitness: {1}".format(self.assignment, self.fitness)