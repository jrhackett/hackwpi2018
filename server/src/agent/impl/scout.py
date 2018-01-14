from server.src.agent.base_agent import BaseAgent
from server.src.agent.agents import AgentType
from server.src.map.resources import ResourceType


class Scout(BaseAgent):

    def __init__(self):
        super().__init__()
        self.resource_skills = {
            ResourceType.COAL: 20,
            ResourceType.COPPER: 20,
            ResourceType.FOOD: 20,
            ResourceType.GOLD: 20,
            ResourceType.IRON: 20,
            ResourceType.OIL: 20,
            ResourceType.WATER: 20,
            ResourceType.WOOD: 20
        }
        self.speed = 5
        self.attack = 10
        self.defense = 10
        self.health = 25
        self.symbol = "S"
        self.agent_type = AgentType.SCOUT
