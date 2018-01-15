import logging
import random
import time

from typing import List
from server.src.engine.active_entity import ActiveEntity

LOG = logging.getLogger(__name__)


class GameEngine:
    """
    High level class that handles the execution of the simulation.  Simulation is based on 'ticks', where all the
    actions in a tick are executed before moving on to the next tick.  On creation, user can specify the number of ticks
    that should be executed and the time delay between ticks (for visualization purposes)
    """
    def __init__(self, number_of_ticks: int, time_per_tick: int = 0.0):
        self.number_of_ticks = number_of_ticks
        self.current_tick = 0
        self.time_per_tick = time_per_tick
        self.is_running = False
        self.entities: List[ActiveEntity] = []

    def run(self, shuffle_entities: bool = False):
        """
        Runs all of the ticks in the engine until the tick limit is reached.  Should be used if the simulation is being
        run in a threaded context.
        :param shuffle_entities: boolean indicating if the order in which entities actions are performed should be
                                 randomized each tick
        :return:
        """
        while self.current_tick < self.number_of_ticks:
            self.handle_tick(shuffle_entities=shuffle_entities)
            if self.time_per_tick:
                time.sleep(self.time_per_tick)

    def handle_tick(self, shuffle_entities: bool = False):
        """
        Performs all of the actions in a single tick
        :param shuffle_entities: boolean indicating if the order in which entities actions are performed should be
                                 randomized each tick
        :return:
        """
        LOG.debug("Starting execution of tick <%s>...", self.current_tick)
        if shuffle_entities:
            LOG.debug("Randomizing order entities will be handled.")
            random.shuffle(self.entities)

        for entity in self.entities:
            LOG.debug("Handling entity <%s> (instance of %s)", entity.id, entity.__class__)
            entity.perform_actions()

        LOG.debug("Finshed execution of tick <%s>.", self.current_tick)
        self.current_tick += 1
