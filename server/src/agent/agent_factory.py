from server.src.agent import impl
from server.src.agent.agents import AgentType
from server.src.agent.base_agent import BaseAgent


class AgentFactory:
    """
    Handles the creation of any new agents. New agents should only be created via the factory and never directly by
    their init method.
    """

    NEXT_AGENT_ID = 1000

    @staticmethod
    def __get_next_id() -> int:
        """
        Factory maintains a static agent ID number that's incremented with each agent created.  This ensures that every
        agent will be generated with a unique ID number
        :return: integer representing the next ID that will be assigned to an agent.
        """
        agent_id = AgentFactory.NEXT_AGENT_ID
        AgentFactory.NEXT_AGENT_ID += 1
        return agent_id

    @staticmethod
    def make_agent(agent_type: AgentType) -> BaseAgent:
        """
        Creates a new ID'ed agent corresponding to the provided agent type enumeration
        :param agent_type: enumerated agent type
        :return: BaseAgent
        """
        if agent_type == AgentType.SCOUT:
            agent = impl.Scout()
        elif agent_type == AgentType.WARRIOR:
            agent = impl.Warrior()
        elif agent_type == AgentType.WORKER:
            agent = impl.Worker()
        else:
            raise NotImplementedError('Provided agent type {} has not been implemented!'.format(agent_type))

        agent.id = AgentFactory.__get_next_id()
        return agent
