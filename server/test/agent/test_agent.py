import pytest
from typing import Dict
from server.src.map.resources import ResourceType
from server.src.agent.agents import AgentType
from server.src.agent import impl


class TestAgent:

    @pytest.mark.parametrize('agent_class, expected_type, expected_symbol', [
        (impl.Worker, AgentType.WORKER, 'P')
    ])
    def test_agent_symbols_and_enumerations(self, agent_class, expected_type: AgentType, expected_symbol: str):
        agent: impl.BaseAgent = agent_class()
        assert expected_type == agent.agent_type
        assert expected_symbol == agent.symbol

    def test_worker_stats(self):
        agent: impl.BaseAgent = impl.Worker()
        expectedSkills = {
            ResourceType.COAL: 50,
            ResourceType.COPPER: 50,
            ResourceType.FOOD: 50,
            ResourceType.GOLD: 50,
            ResourceType.IRON: 50,
            ResourceType.OIL: 50,
            ResourceType.WATER: 50,
            ResourceType.WOOD: 50
        }
        for skill, value in agent.resource_skills.items():
            assert value == expectedSkills.get(skill)
        assert agent.speed == 30
        assert agent.attack == 5
        assert agent.defense == 5
