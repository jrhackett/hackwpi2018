from abc import ABC
from server.src.agent.agents import AgentType


class BaseAgent(ABC):

    x: int
    y: int
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
