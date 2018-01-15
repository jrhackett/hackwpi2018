from server.src.map.tiles.base_tile import BaseTile
from server.src.map.resources import ResourceType


class FoodTile(BaseTile):
    """
    Food resource
    """
    def __init__(self):
        super().__init__()
        self.resource_type = ResourceType.FOOD
        self.symbol = "F"
