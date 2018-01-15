from server.src.agent.actions.base_action import BaseAction


class MoveAction(BaseAction):
    """
    Handles movement between tiles for an agent.
    """
    def __init__(self, performing_agent, target_x: int, target_y: int):
        super().__init__(performing_agent)
        self.target_x = target_x
        self.target_y = target_y

    def perform_action(self):
        """
        Moves the agent to the provided position, if the position is within the agents speed. Otherwise, moves the agent
        as far as it could possibly get to the position in this tick.
        :return:
        """
        x_diff: int = abs(self.performing_agent.point.x - self.target_x)
        y_diff: int = abs(self.performing_agent.point.y - self.target_y)
        if x_diff + y_diff <= self.performing_agent.speed:
            self.performing_agent.point.set_point(self.target_x, self.target_y)
        else:
            distance_traveled: int = 0
            while distance_traveled < self.performing_agent.speed:
                if x_diff > 0:
                    self.performing_agent.point.set_point(self.performing_agent.point.x + 1, self.performing_agent.point.y)
                    distance_traveled += 1
                    x_diff -= 1
                if distance_traveled >= self.performing_agent.speed:
                    break
                if y_diff > 0:
                    self.performing_agent.point.set_point(self.performing_agent.point.x, self.performing_agent.point.y + 1)
                    distance_traveled += 1
                    y_diff -= 1
