from server.src.agent import impl
from server.src.agent.agents import AgentType


class AgentFactory:

    @staticmethod
    def make_agent(agent_type: AgentType):
        if agent_type == AgentType.SCOUT:
            return impl.Scout()
        if agent_type == AgentType.WARRIOR:
            return impl.Warrior()
        if agent_type == AgentType.WORKER:
            return impl.Worker()
