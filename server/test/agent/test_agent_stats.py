import pytest
from server.src.map.resources import ResourceType
from server.src.agent.agents import AgentType
from server.src.agent import impl


class TestAgent:

    @pytest.mark.parametrize('agent_class, expected_type, expected_symbol', [
        (impl.Scout, AgentType.SCOUT, 'S'),
        (impl.Warrior, AgentType.WARRIOR, 'F'),
        (impl.Worker, AgentType.WORKER, 'P')
    ])
    def test_agent_symbols_and_enumerations(self, agent_class, expected_type: AgentType, expected_symbol: str):
        agent: impl.BaseAgent = agent_class()
        assert expected_type == agent.agent_type
        assert expected_symbol == agent.symbol

    @pytest.mark.parametrize('agent_class', [
        impl.Scout,
        impl.Warrior,
        impl.Worker
    ])
    def test_agent_common_stats(self, agent_class):
        agent: impl.BaseAgent = agent_class()
        assert agent.hunger == 100
        assert agent.thirst == 100
        assert agent.vision == 4

    def test_worker_stats(self):
        agent: impl.BaseAgent = impl.Worker()
        expected_skills = {
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
            assert value == expected_skills.get(skill)
        assert agent.speed == 30
        assert agent.attack == 5
        assert agent.defense == 5
        assert agent.health == 50

    def test_warrior_stats(self):
        agent: impl.BaseAgent = impl.Warrior()
        expected_skills = {
            ResourceType.COAL: 10,
            ResourceType.COPPER: 10,
            ResourceType.FOOD: 10,
            ResourceType.GOLD: 10,
            ResourceType.IRON: 10,
            ResourceType.OIL: 10,
            ResourceType.WATER: 10,
            ResourceType.WOOD: 10
        }
        for skill, value in agent.resource_skills.items():
            assert value == expected_skills.get(skill)
        assert agent.speed == 40
        assert agent.attack == 25
        assert agent.defense == 25
        assert agent.health == 100

    def test_scout_stats(self):
        agent: impl.BaseAgent = impl.Scout()
        expected_skills = {
            ResourceType.COAL: 20,
            ResourceType.COPPER: 20,
            ResourceType.FOOD: 20,
            ResourceType.GOLD: 20,
            ResourceType.IRON: 20,
            ResourceType.OIL: 20,
            ResourceType.WATER: 20,
            ResourceType.WOOD: 20
        }
        for skill, value in agent.resource_skills.items():
            assert value == expected_skills.get(skill)
        assert agent.speed == 60
        assert agent.attack == 10
        assert agent.defense == 10
        assert agent.health == 25
