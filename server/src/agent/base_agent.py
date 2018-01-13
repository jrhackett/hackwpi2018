from typing import Dict
from server.src.agent.agents import AgentType
from server.src.map.resources import ResourceType


class BaseAgent:

    x: int
    y: int
    resource_skills: dict
    speed: int
    attack: int
    defense: int
    symbol: str
    agent_type: AgentType
