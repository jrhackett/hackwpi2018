import abc

class ActiveEntity(abc.ABC):

    @abc.abstractmethod
    def perform_action(self):
        pass

    @abc.abstractmethod
    def get_id(self) -> int:
        pass
