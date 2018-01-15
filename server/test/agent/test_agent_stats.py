import pytest
from server.src.map.resources import ResourceType
from server.src.agent.agents import AgentType
from server.src.agent.agent_factory import AgentFactory
from server.src.agent.base_agent import BaseAgent


class TestAgent:

    @pytest.mark.parametrize('agent_type, expected_symbol', [
        (AgentType.SCOUT, 'S'),
        (AgentType.WARRIOR, 'F'),
        (AgentType.WORKER, 'P')
    ])
    def test_agent_symbols_and_enumerations(self, agent_type: AgentType, expected_symbol: str):
        agent: BaseAgent = AgentFactory.make_agent(agent_type)
        assert agent_type == agent.agent_type
        assert expected_symbol == agent.symbol

    @pytest.mark.parametrize('agent_type', [
        AgentType.SCOUT,
        AgentType.WARRIOR,
        AgentType.WORKER
    ])
    def test_agent_common_stats(self, agent_type):
        agent: BaseAgent = AgentFactory.make_agent(agent_type)
        assert agent.hunger == 100
        assert agent.thirst == 100
        assert agent.vision == 4

    def test_worker_stats(self):
        agent: BaseAgent = AgentFactory.make_agent(AgentType.WORKER)
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
        assert agent.speed == 2
        assert agent.attack == 5
        assert agent.defense == 5
        assert agent.health == 50

    def test_warrior_stats(self):
        agent: BaseAgent = AgentFactory.make_agent(AgentType.WARRIOR)
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
        assert agent.speed == 3
        assert agent.attack == 25
        assert agent.defense == 25
        assert agent.health == 100

    def test_scout_stats(self):
        agent: BaseAgent = AgentFactory.make_agent(AgentType.SCOUT)
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
        assert agent.speed == 5
        assert agent.attack == 10
        assert agent.defense == 10
        assert agent.health == 25
