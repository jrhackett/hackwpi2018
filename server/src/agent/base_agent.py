from abc import ABC
from server.src.agent.agents import AgentType


class BaseAgent(ABC):

    x: int = 0
    y: int = 0
    resource_skills: dict
    speed: int
    attack: int
    defense: int
    health: int
    hunger: int = 100
    thirst: int = 100
    vision: int = 4
    symbol: str
    agent_type: AgentType

    def move(self, x, y):
        self.x = x
        self.y = y

    def get_position(self):
        return self.x, self.y
