from server.src.map.tiles.base_tile import BaseTile
from server.src.map.resources import ResourceType


class NoneTile(BaseTile):

    def __init__(self):
        super().__init__()
        self.resource_type = ResourceType.NONE
        self.quantity = 0
        self.symbol = " "
