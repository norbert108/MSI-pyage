from pyage.core import address
from pyage.core.agent.agent import unnamed_agents, generate_agents, Agent
from pyage.core.agent.aggregate import AggregateAgent
from pyage.core.emas import EmasService
from pyage.core.locator import GridLocator
from pyage.core.migration import ParentMigration
from pyage.core.stats.gnuplot import TimeStatistics, StepStatistics
from pyage.core.stop_condition import StepLimitStopCondition, MinimumFitnessStopCondition
from pyage.solutions.evolution.crossover import SinglePointCrossover
from pyage.solutions.evolution.evaluation import FloatRastriginEvaluation
from pyage.solutions.evolution.initializer import float_emas_initializer
from pyage.solutions.evolution.initializer import emas_initializer
from pyage.solutions.evolution.mutation import UniformFloatMutation
from pyage.elect.naming_service import NamingService

from pyage.solutions.evolution.initializer import FloatInitializer
from initializer import cnf_emas_initializer

from evaluation import CNFEvaluation
from pyage.solutions.evolution.selection import TournamentSelection
from crossover import CNFCrossover
from mutation import CNFMutation
from initializer import CNFInitializer
from genotype import CNF

import os
import Pyro4

from pyage.core.locator import Pyro4Locator

from pyage.core.locator import RandomLocator
from pyage.core.migration import NoMigration

agents_count = 1
agents = generate_agents("agent", agents_count, Agent)

stop_condition = lambda: MinimumFitnessStopCondition(2, 1000)

# agg_size = 40
# aggregated_agents = lambda: cnf_emas_initializer(energy=100, size=50, description="123321", variables=3)
# aggregated_agents = lambda: CNFInitializer("123231", 3)

emas = EmasService

minimal_energy = lambda: 0
reproduction_minimum = lambda: 90
migration_minimum = lambda: 120
newborn_energy = lambda: 1007
transferred_energy = lambda: 40

evaluation = CNFEvaluation()
crossover = CNFCrossover(agents_count)
mutation = CNFMutation()
selection = TournamentSelection(size=agents_count, tournament_size=agents_count)

operators = lambda: [evaluation, selection, crossover, mutation]

initializer = lambda: CNFInitializer(description=[1,2,-1,3,-3,3,1,2,3,-1, 2, 3, -3,-2,-1], variables=3, size=agents_count)

address_provider = address.SequenceAddressProvider

migration = NoMigration
locator = RandomLocator
# ns_hostname = lambda: 'localhost'
# pyro_daemon = Pyro4.Daemon()
# daemon = lambda: pyro_daemon
#
naming_service = lambda: NamingService(agents_count)

stats = StepStatistics