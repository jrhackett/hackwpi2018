import logging

from server.src.agent.actions import impl as actions_impl
from server.src.agent.agents import AgentType
from server.src.engine.active_entity import ActiveEntity
from server.src.point.point import Point

LOG = logging.getLogger(__name__)


class BaseAgent(ActiveEntity):
    """
    Serves as a basis for all agents
    """
    def __init__(self):
        self.point: Point = Point()
        self.id: int = 0
        self.resource_skills: dict = {}
        self.speed: int = 0
        self.attack: int = 0
        self.defense: int = 0
        self.health: int = 0
        self.hunger: int = 100
        self.thirst: int = 100
        self.vision: int = 4
        self.symbol: str = ""
        self.agent_type: AgentType
        self.actions: list = []

    def perform_actions(self):
        """
        Executes all of the actions that are currently in this agent's queue, and clears the queue as they are executed
        :return:
        """
        for action in self.actions:
            action.perform_action()
            if action.ticks_required == action.ticks_executed:
                self.actions.remove(action)

    def add_move_action(self, target_x: int, target_y: int):
        """
        Add a MoveAction to the agent's queue
        :param target_x: x position to move to
        :param target_y: y position to move to
        :return:
        """
        move_action = actions_impl.MoveAction(self, target_x, target_y)
        self.actions.append(move_action)

    def add_collect_action(self):
        """
        Adds a CollectAction to the agent's queue
        :return:
        """
        collect_action = actions_impl.CollectAction(self)
        self.actions.append(collect_action)
