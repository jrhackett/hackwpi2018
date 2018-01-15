import logging
import pytest

from server.src.agent.agent_factory import AgentFactory
from server.src.agent.agents import AgentType
from server.src.engine.game_engine import GameEngine
from server.src.map.generator.yaml_map_maker import YamlMapMaker
from server.src.map.map import Map

LOG = logging.getLogger(__name__)


@pytest.fixture(scope='function')
def blank_map() -> Map:
    blank_map_data = {
        'map':
            {
                'width': 100,
                'height': 100,
                'density': 0.0
            }
    }
    map_maker = YamlMapMaker(yaml_data=blank_map_data)
    return map_maker.generate_map()


class TestGameEngine:

    def test_empty_engine_runs_correct_number_of_ticks(self):
        ticks = 10
        g = GameEngine(ticks)
        assert ticks == g.number_of_ticks
        g.run()
        assert ticks == g.current_tick

    def test_single_tick_single_agent_movement_on_empty_map(self):
        ticks = 1
        g = GameEngine(ticks)
        # Create the worker at 2, 2, and expect movement to 3, 3
        worker = AgentFactory.make_agent(AgentType.WORKER)
        worker.point.x, worker.point.y = 2, 2
        worker.add_move_action(3, 3)
        g.entities.append(worker)
        g.handle_tick()

        assert 3 == worker.point.x
        assert 3 == worker.point.y

    def test_single_tick_mutli_agent_movement_on_empty_map(self):
        ticks = 1
        g = GameEngine(ticks)
        # Create workers at 0,0 -> 0,10 and expect horizontal movement from all
        workers = []
        for j in range(10):
            worker = AgentFactory.make_agent(AgentType.WORKER)
            worker.point.x, worker.point.y = 0, j
            worker.add_move_action(1, j)
            g.entities.append(worker)
            workers.append(worker)

        g.handle_tick()
        for j in range(10):
            assert 1 == workers[j].point.x
            assert j == workers[j].point.y

    def test_multi_tick_single_agent_movement_on_empty_map(self):
        ticks = 10
        g = GameEngine(ticks)
        # Create worker at 5, 0 and expect vertical movement down 10 total positions
        worker = AgentFactory.make_agent(AgentType.WORKER)
        worker.point.x, worker.point.y = 5, 0
        g.entities.append(worker)

        for j in range(10):
            worker.add_move_action(worker.point.x, j + 1)
            g.handle_tick()
            assert 5 == worker.point.x
            assert j + 1 == worker.point.y

    def test_multi_agent_multi_tick_movement_on_empty_map(self):
        ticks = 5
        g = GameEngine(ticks)
        # Create workers at i, 0 and expect vertical movement down 5 positions
        workers = []
        for i in range(5):
            worker = AgentFactory.make_agent(AgentType.WORKER)
            worker.point.x, worker.point.y = i, 0
            workers.append(worker)
            g.entities.append(worker)

        for tick in range(5):
            for i in range(5):
                workers[i].add_move_action(workers[i].point.x, tick + 1)
            g.handle_tick()
            for i in range(5):
                assert i == workers[i].point.x
                assert tick + 1 == workers[i].point.y
