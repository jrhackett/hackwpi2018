from server.src.engine.game_engine import GameEngine


class TestGameEngine:

    def test_empty_engine_runs_correct_number_of_ticks(self):
        ticks = 10
        g = GameEngine(ticks, time_per_tick=0)
        assert ticks == g.number_of_ticks
        g.run()
        assert ticks == g.current_tick
