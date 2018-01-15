from server.src.map.tiles.base_tile import BaseTile
from server.src.map.resources import ResourceType


class WaterTile(BaseTile):
    """
    Water resource
    """
    def __init__(self):
        super().__init__()
        self.resource_type = ResourceType.WATER
        self.symbol = '~'
