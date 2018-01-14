from server.src.agent.agents import AgentType


class BaseAgent:

    x: int
    y: int
    resource_skills: dict
    speed: int
    attack: int
    defense: int
    health: int
    hunger: int = 100
    thirst: int = 100
    symbol: str
    agent_type: AgentType

    # TODO take into consideration defense
    def take_damage(self, hp):
        self.health -= hp
        return self.health <= 0

    def heal(self, hp):
        self.health += hp
