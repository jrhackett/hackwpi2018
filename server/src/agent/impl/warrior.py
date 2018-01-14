from server.src.agent.base_agent import BaseAgent
from server.src.agent.agents import AgentType
from server.src.map.resources import ResourceType


class Warrior(BaseAgent):

    def __init__(self):
        super().__init__()
        self.resource_skills = {
            ResourceType.COAL: 10,
            ResourceType.COPPER: 10,
            ResourceType.FOOD: 10,
            ResourceType.GOLD: 10,
            ResourceType.IRON: 10,
            ResourceType.OIL: 10,
            ResourceType.WATER: 10,
            ResourceType.WOOD: 10
        }
        self.speed = 40
        self.attack = 25
        self.defense = 25
        self.health = 100
        self.symbol = "F"
        self.agent_type = AgentType.WARRIOR
