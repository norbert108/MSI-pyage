from pyage.core import address
from pyage.core.agent.agent import unnamed_agents, generate_agents, Agent
from pyage.core.agent.aggregate import AggregateAgent
from pyage.core.emas import EmasService
from pyage.core.locator import GridLocator, RowLocator
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

from pyage.core.statistics import TimeStatistics
import os
import Pyro4

from pyage.core.locator import Pyro4Locator

from pyage.core.locator import RandomLocator
from pyage.core.migration import NoMigration

import logging

logger = logging.getLogger(__name__)

agents_count = 1
logger.debug("EVO, %s agents", agents_count)
agents = unnamed_agents(agents_count, AggregateAgent)

stop_condition = lambda: MinimumFitnessStopCondition(99, 1000)

# agg_size = 40
aggregated_agents = lambda: cnf_emas_initializer(energy=100, size=50, description=[-3, -2, 5, -6, -7, -4, -4, -9, -8, -4, 5, -3, -6, 3, -10, -2, -2, 9, -10, -5, -10, -4, 1, 4, 7, -9, 6, -10, -7, 2, -5, -8, -1, 6, -1, 1, -8, -5, -7, -1, -3, -2, -10, 6, -9, -8, -10, -3, -4, 6, -10, 3, 4, -1, -10, 1, -2, 1, 4, -1, -6, 6, -9, -9, 2, -2, -5, 3, -6, -3, -6, 6, 3, 5, -1, -6, 2, -9, 8, 10, -1, -4, 3, 5, -10, -1, 4, -5, -9, -2, -5, -1, 5, -2, -2, -3, 4, -10, -10, 2, -6, 3, -5, -3, 6, -5, 4, -1, -4, 2, 1, -9, -7, 6, 7, 1, -7, -2, 9, -9, -10, 5, -2, -3, -5, -2, 10, 10, 7, 10, -3, 5, 7, -5, -4, -5, 9, -1, -7, -6, -2, -5, -4, -7, -2, -10, -8, -5, 6, -6, -7, -5, -7, 5, 10, -9, -7, -6, -4, -2, -7, -2, -7, 9, -7, -3, 5, -9, -4, -1, -4, -6, -2, 9, 4, -1, -8, -1, -8, -6, 5, -9, -2, -9, -3, -3, 10, -2, -5, 10, -10, -1, -4, -6, -3, -1, 5, -10, -1, 3, 2, 3, -9, -4, -3, 1, -6, -9, 1, -5, -8, 8, -4, -2, -5, -8, 10, -4, 9, -1, -4, 1, 1, 5, -4, 3, -3, -9, -2, -4, -4, 2, -7, -5, 5, -8, -7, -3, 3, -4, 8, -8, -8, -6, -5, -8, -4, -5, -5, -10, 1, -10, 8, -7, -10, 9, 8, -3, 1, -3, -1, -6, 8, -6, -3, -2, -7, -8, 2, -6, 10, -2, -6, 7, 4, -10, -4, -10, 1, -1, -9, -3, -3, -7, -5, -5, -8, 2, 6, -3, -3, -10, -8, -3, -3, -6, -1, -10, 5, -4], variables=10)
# aggregated_agents = lambda: CNFInitializer("123231", 3)

emas = EmasService

minimal_energy = lambda: 0
reproduction_minimum = lambda: 90
migration_minimum = lambda: 120
newborn_energy = lambda: 1007
transferred_energy = lambda: 40

evaluation = CNFEvaluation
crossover = lambda: CNFCrossover(agents_count)
mutation = CNFMutation

address_provider = address.SequenceAddressProvider

migration = ParentMigration
locator = GridLocator

naming_service = lambda: NamingService(agents_count)

stats = TimeStatistics