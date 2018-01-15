import pytest
import math
import logging

from server.src.agent.base_agent import BaseAgent
from server.src.agent.agents import AgentType
from server.src.agent.agent_factory import AgentFactory

LOG = logging.getLogger(__name__)


@pytest.mark.parametrize('agent_type', [
    AgentType.SCOUT,
    AgentType.WARRIOR,
    AgentType.WORKER
])
class TestAgent:

    def test_basic_movement_in_one_positive_direction(self, agent_type):
        agent: BaseAgent = AgentFactory.make_agent(agent_type)
        x, y = agent.point.x, agent.point.y
        agent.add_move_action(x + 1, y)
        agent.perform_actions()
        new_x, new_y = agent.point.x, agent.point.y
        assert new_x == x + 1
        assert new_y == y

    def test_basic_movement_in_two_positive_directions(self, agent_type):
        agent: BaseAgent = AgentFactory.make_agent(agent_type)
        pos = agent.point.x, agent.point.y
        agent.add_move_action(pos[0] + 1, pos[1] + 1)
        agent.perform_actions()
        new_pos = agent.point.x, agent.point.y
        assert new_pos[0] == pos[0] + 1
        assert new_pos[1] == pos[1] + 1

    def test_restricted_movement_in_one_positive_direction(self, agent_type):
        agent: BaseAgent = AgentFactory.make_agent(agent_type)
        pos = agent.point.x, agent.point.y
        agent.add_move_action(pos[0] + 20, pos[1])
        agent.perform_actions()
        new_pos = agent.point.x, agent.point.y
        assert new_pos[0] == pos[0] + agent.speed
        assert new_pos[1] == pos[1]

    def test_restricted_movement_in_two_positive_directions(self, agent_type):
        agent: BaseAgent = AgentFactory.make_agent(agent_type)
        pos = agent.point.x, agent.point.y
        agent.add_move_action(pos[0] + 20, pos[1] + 20)
        agent.perform_actions()
        new_pos = agent.point.x, agent.point.y
        assert new_pos[0] == pos[0] + math.ceil(agent.speed / 2)
        assert new_pos[1] == pos[1] + math.floor(agent.speed / 2)

    def test_basic_movement_in_one_negative_direction(self, agent_type):
        agent: BaseAgent = AgentFactory.make_agent(agent_type)
        pos = agent.point.x, agent.point.y
        agent.add_move_action(pos[0] - 1, pos[1])
        agent.perform_actions()
        new_pos = agent.point.x, agent.point.y
        assert new_pos[0] == pos[0] - 1
        assert new_pos[1] == pos[1]

    def test_basic_movement_in_two_negative_directions(self, agent_type):
        agent: BaseAgent = AgentFactory.make_agent(agent_type)
        pos = agent.point.x, agent.point.y
        agent.add_move_action(pos[0] - 1, pos[1] - 1)
        agent.perform_actions()
        new_pos = agent.point.x, agent.point.y
        assert new_pos[0] == pos[0] - 1
        assert new_pos[1] == pos[1] - 1
