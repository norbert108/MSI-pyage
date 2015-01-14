from pyage.core.stop_condition import StopCondition

class MinimumFitnessStopCondition(StopCondition):
    def __init__(self, minimal_fitness, step_limit):
        super(MinimumFitnessStopCondition, self).__init__()
        self.minimal_fitness = minimal_fitness
        self.step_limit = step_limit

    def should_stop(self, workplace):
        return workplace.get_fitness() >= self.minimal_fitness or 0 < self.step_limit <= workplace.steps