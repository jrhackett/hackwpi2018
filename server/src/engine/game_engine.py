import logging
import random
import time

from typing import List
from server.src.engine.active_entity import ActiveEntity


LOG = logging.getLogger(__name__)

class GameEngine:

    def __init__(self, number_of_ticks: int, time_per_tick: int = 0.1):
        self.number_of_ticks = number_of_ticks
        self.current_tick = 0
        self.time_per_tick = time_per_tick
        self.is_running = False
        self.entities: List[ActiveEntity] = []

    def run(self):
        pass

    def handle_tick(self, shuffle_entities: bool = True):
        LOG.debug("Starting execution of tick <%s>...", self.current_tick)
        if shuffle_entities:
            LOG.debug("Randomizing order entities will be handled.")
            random.shuffle(self.entities)

        for entity in self.entities:
            LOG.debug("Handling entity <%s> (instance of %s)", entity.get_id(), entity.__class__)
            entity.perform_action()

        LOG.debug("Finshed execution of tick <%s>.", self.current_tick)
