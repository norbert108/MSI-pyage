from pyage.core import address
from pyage.core.agent.agent import unnamed_agents
from pyage.core.agent.aggregate import AggregateAgent
from pyage.core.emas import EmasService
from pyage.core.locator import GridLocator
from pyage.core.migration import ParentMigration
from pyage.core.stats.gnuplot import TimeStatistics, StepStatistics
from pyage.core.stop_condition import StepLimitStopCondition
from pyage.solutions.evolution.crossover import SinglePointCrossover
from pyage.solutions.evolution.evaluation import FloatRastriginEvaluation
from pyage.solutions.evolution.initializer import float_emas_initializer
from pyage.solutions.evolution.mutation import UniformFloatMutation
from pyage.elect.naming_service import NamingService

from evaluation import CNFEvaluation
from pyage.solutions.evolution.selection import TournamentSelection
from crossover import CNFCrossover
from mutation import CNFMutation
from initializer import CNFInitializer
from genotype import CNF

agents_count = 5
agents = unnamed_agents(agents_count, AggregateAgent)

stop_condition = lambda: StepLimitStopCondition(100)

# aggregated_agents = lambda: float_emas_initializer(10, energy=100, size=50, lowerbound=-10, upperbound=10)
aggregated_agents = lambda: CNFInitializer("123231", 3)

emas = EmasService

minimal_energy = lambda: 0
reproduction_minimum = lambda: 90
migration_minimum = lambda: 120
newborn_energy = lambda: 100
transferred_energy = lambda: 40

evaluation = CNFEvaluation
crossover = CNFCrossover
mutation = CNFMutation
selection = TournamentSelection

operators = lambda: [evaluation, selection, crossover, mutation]

# initializer = lambda: CNFInitializer("123231", 3)

address_provider = address.SequenceAddressProvider

migration = ParentMigration
locator = GridLocator

naming_service = lambda: NamingService(starting_number=2)

stats = StepStatistics