from server.src.agent.base_agent import BaseAgent
from server.src.agent.agents import AgentType
from server.src.map.resources import ResourceType


class Worker(BaseAgent):
    """
    Worker agent excels at resource collection, but moves slowly and is moderately fragile.
    """
    def __init__(self):
        super().__init__()
        self.resource_skills = {
            ResourceType.COAL: 50,
            ResourceType.COPPER: 50,
            ResourceType.FOOD: 50,
            ResourceType.GOLD: 50,
            ResourceType.IRON: 50,
            ResourceType.OIL: 50,
            ResourceType.WATER: 50,
            ResourceType.WOOD: 50
        }
        self.speed = 2
        self.attack = 5
        self.defense = 5
        self.health = 50
        self.symbol = "P"
        self.agent_type = AgentType.WORKER
