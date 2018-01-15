import logging
from abc import ABC
from server.src.agent.agents import AgentType

LOG = logging.getLogger(__name__)


class BaseAgent(ABC):

    x: int = 0
    y: int = 0
    resource_skills: dict = {}
    speed: int = 0
    attack: int = 0
    defense: int = 0
    health: int = 0
    hunger: int = 100
    thirst: int = 100
    vision: int = 4
    symbol: str = ""
    agent_type: AgentType

    def move(self, x, y):
        x_diff = abs(self.x - x)
        y_diff = abs(self.y - y)
        if x_diff + y_diff <= self.speed:
            self.x = x
            self.y = y
        else:
            c = 0
            while c < self.speed:
                if x_diff > 0:
                    self.x += 1
                    c += 1
                    x_diff -= 1
                if c >= self.speed:
                    break
                if y_diff > 0:
                    self.y += 1
                    c += 1
                    y_diff -= 1

    def get_position(self):
        return self.x, self.y

    def get_speed(self):
        return self.speed
