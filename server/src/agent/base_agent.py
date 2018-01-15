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

    def move(self, x: int, y: int):
        x_diff: int = abs(self.point.x - x)
        y_diff: int = abs(self.point.y - y)
        if x_diff + y_diff <= self.speed:
            self.point.set_point(x, y)
        else:
            c: int = 0
            while c < self.speed:
                if x_diff > 0:
                    self.point.set_point(self.point.x + 1, self.point.y)
                    c += 1
                    x_diff -= 1
                if c >= self.speed:
                    break
                if y_diff > 0:
                    self.point.set_point(self.point.x, self.point.y + 1)
                    c += 1
                    y_diff -= 1

    def get_position(self):
        return self.point.x, self.point.y

    def get_speed(self):
        return self.speed
