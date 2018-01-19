import pytest

from server.src.agent.agent_factory import AgentFactory
from server.src.agent.agents import AgentType
from server.src.agent.actions.base_action import BaseAction
from server.src.engine.game_engine import GameEngine


class TestActionDurations:

    class OneTickAction(BaseAction):
        def __init__(self, performing_agent):
            super().__init__(performing_agent)
            self.ticks_required = 1

        def perform_action(self):
            self.ticks_executed += 1

    class TwoTickAction(BaseAction):
        def __init__(self, performing_agent):
            super().__init__(performing_agent)
            self.ticks_required = 2

        def perform_action(self):
            self.ticks_executed += 1

    class FiveTickAction(BaseAction):
        def __init__(self, performing_agent):
            super().__init__(performing_agent)
            self.ticks_required = 5

        def perform_action(self):
            self.ticks_executed += 1

    @pytest.mark.parametrize('tick_type, ticks_required', [
        (OneTickAction, 1),
        (TwoTickAction, 2),
        (FiveTickAction, 5)])
    def test_varying_length_actions(self, tick_type: BaseAction.__class__, ticks_required: int):
        g = GameEngine(ticks_required)
        worker = AgentFactory.make_agent(AgentType.WORKER)
        action = tick_type(worker)
        worker.actions.append(action)
        g.entities.append(worker)
        assert 0 == action.ticks_executed
        assert worker.actions
        for tick in range(ticks_required):
            g.handle_tick()
            if tick + 1 == ticks_required:
                break
            else:
                assert worker.actions
        assert not worker.actions


    def test_single_tick_action_ends_after_tick(self):
        g = GameEngine(1)
        worker = AgentFactory.make_agent(AgentType.WORKER)
        action = TestActionDurations.OneTickAction(worker)
        worker.actions.append(action)
        g.entities.append(worker)
        assert 0 == action.ticks_executed
        g.handle_tick()
        assert not worker.actions

    def test_two_tick_action_ends_after_two_ticks(self):
        g = GameEngine(2)
        worker = AgentFactory.make_agent(AgentType.WORKER)
        action = TestActionDurations.TwoTickAction(worker)
        worker.actions.append(action)
        g.entities.append(worker)
        assert 0 == action.ticks_executed
        g.handle_tick()
        assert worker.actions
        g.handle_tick()
        assert not worker.actions

