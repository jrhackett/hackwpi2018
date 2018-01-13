from typing import Dict
from server.src.agent.agents import AgentType


class BaseAgent:

    x: int
    y: int
    resource_skills: Dict[str, int]
    speed: int
    attack: int
    defense: int
    symbol: str
    agent_type: AgentType
