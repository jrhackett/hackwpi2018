class BaseAction:
    """
    Provides an interface for any action that can be performed by an agent.
    """

    priority: int
    ticks_required: int

    def __init__(self, performing_agent):
        self.performing_agent = performing_agent
        self.ticks_executed = 0

    def perform_action(self):
        pass
