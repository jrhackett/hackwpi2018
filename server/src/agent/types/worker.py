from server.src.agent.types.base_agent import BaseAgent
from server.src.agent.agents import AgentType


class Worker(BaseAgent):

    def __init__(self):
        super().__init__()
        self.resource_skills = {
            "coal": 50,
            "copper": 50,
            "food": 50,
            "gold": 50,
            "iron": 50,
            "oil": 50,
            "water": 50,
            "wood": 50
        }
        self.speed = 30
        self.attack = 5
        self.defense = 5
        self.symbol = "P"
        self.agent_type = AgentType.WORKER
