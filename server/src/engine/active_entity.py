import abc


class ActiveEntity(abc.ABC):
    """
    Any object that can be handled by the game engine must be capable of having these functions performed on it.  It
    provides a common interface for all interactive objects
    """
    def __init__(self):
        self.id: int = 0

    @abc.abstractmethod
    def perform_actions(self):
        pass
