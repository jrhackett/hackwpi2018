import logging
from abc import ABC
from server.src.agent.agents import AgentType
from server.src.point.point import Point

LOG = logging.getLogger(__name__)


class BaseAgent(ABC):

    point: Point = Point()
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
        x_diff = abs(self.point.get_x() - x)
        y_diff = abs(self.point.get_y() - y)
        if x_diff + y_diff <= self.speed:
            self.point.set_point(x, y)
        else:
            c = 0
            while c < self.speed:
                if x_diff > 0:
                    self.point.set_x(self.point.get_x() + 1)
                    c += 1
                    x_diff -= 1
                if c >= self.speed:
                    break
                if y_diff > 0:
                    self.point.set_y(self.point.get_y() + 1)
                    c += 1
                    y_diff -= 1

    def get_position(self):
        return self.point.get_point()

    def get_speed(self):
        return self.speed
