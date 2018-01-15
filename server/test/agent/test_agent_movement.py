import pytest
import math
import logging
from server.src.agent import impl

LOG = logging.getLogger(__name__)


class TestAgent:

    @pytest.mark.parametrize('agent_class', [
        impl.Scout,
        impl.Warrior,
        impl.Worker
    ])
    def test_basic_movement_in_one_positive_direction(self, agent_class):
        agent: impl.BaseAgent = agent_class()
        pos = agent.get_position()
        agent.move(pos[0] + 1, pos[1])
        new_pos = agent.get_position()
        assert new_pos[0] == pos[0] + 1
        assert new_pos[1] == pos[1]

    @pytest.mark.parametrize('agent_class', [
        impl.Scout,
        impl.Warrior,
        impl.Worker
    ])
    def test_basic_movement_in_two_positive_directions(self, agent_class):
        agent: impl.BaseAgent = agent_class()
        pos = agent.get_position()
        agent.move(pos[0] + 1, pos[1] + 1)
        new_pos = agent.get_position()
        assert new_pos[0] == pos[0] + 1
        assert new_pos[1] == pos[1] + 1

    @pytest.mark.parametrize('agent_class', [
        impl.Scout,
        impl.Warrior,
        impl.Worker
    ])
    def test_restricted_movement_in_one_positive_direction(self, agent_class):
        agent: impl.BaseAgent = agent_class()
        pos = agent.get_position()
        agent.move(pos[0] + 20, pos[1])
        new_pos = agent.get_position()
        assert new_pos[0] == pos[0] + agent.get_speed()
        assert new_pos[1] == pos[1]

    @pytest.mark.parametrize('agent_class', [
        impl.Scout,
        impl.Warrior,
        impl.Worker
    ])
    def test_restricted_movement_in_two_positive_directions(self, agent_class):
        agent: impl.BaseAgent = agent_class()
        pos = agent.get_position()
        agent.move(pos[0] + 20, pos[1] + 20)
        new_pos = agent.get_position()
        assert new_pos[0] == pos[0] + math.ceil(agent.get_speed() / 2)
        assert new_pos[1] == pos[1] + math.floor(agent.get_speed() / 2)

    @pytest.mark.parametrize('agent_class', [
        impl.Scout,
        impl.Warrior,
        impl.Worker
    ])
    def test_basic_movement_in_one_negative_direction(self, agent_class):
        agent: impl.BaseAgent = agent_class()
        pos = agent.get_position()
        agent.move(pos[0] - 1, pos[1])
        new_pos = agent.get_position()
        assert new_pos[0] == pos[0] - 1
        assert new_pos[1] == pos[1]

    @pytest.mark.parametrize('agent_class', [
        impl.Scout,
        impl.Warrior,
        impl.Worker
    ])
    def test_basic_movement_in_two_negative_directions(self, agent_class):
        agent: impl.BaseAgent = agent_class()
        pos = agent.get_position()
        agent.move(pos[0] - 1, pos[1] - 1)
        new_pos = agent.get_position()
        assert new_pos[0] == pos[0] - 1
        assert new_pos[1] == pos[1] - 1
