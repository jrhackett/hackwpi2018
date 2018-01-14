import pytest
from server.src.agent.agents import AgentType
from server.src.agent import impl


class TestAgent:

    @pytest.mark.parametrize('agent_class', [
        impl.Scout,
        impl.Warrior,
        impl.Worker
    ])
    def test_basic_movement(self, agent_class):
        agent: impl.BaseAgent = agent_class()
        pos = agent.get_position()
        agent.move(pos[0] + 1, pos[1] + 1)
        new_pos = agent.get_position()
        assert new_pos[0] == pos[0] + 1
        assert new_pos[1] == pos[1] + 1
