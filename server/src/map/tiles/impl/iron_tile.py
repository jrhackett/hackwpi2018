from server.src.map.tiles.base_tile import BaseTile
from server.src.map.resources import ResourceType


class IronTile(BaseTile):

    def __init__(self):
        super().__init__()
        self.resource_type = ResourceType.IRON
        self.symbol = "I"
