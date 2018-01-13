import pytest
from server.src.agent.agents import AgentType
from server.src.agent import types


class TestAgent:

    @pytest.mark.parametrize('agent_class, expected_type, expected_symbol', [
        (types.Worker, AgentType.WORKER, 'P')
    ])
    def test_agent_symbols_and_enumerations(self, agent_class, expected_type: AgentType, expected_symbol: str):
        tile: types.BaseAgent = agent_class()
        assert expected_type == tile.agent_type
        assert expected_symbol == tile.symbol
