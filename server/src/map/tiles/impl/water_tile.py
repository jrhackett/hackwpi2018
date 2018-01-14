from swarm_af_server.src.map.tiles.base_tile import BaseTile
from swarm_af_server.src.map.resources import ResourceType


class WaterTile(BaseTile):

    def __init__(self):
        super().__init__()
        self.resource_type = ResourceType.WATER
        self.symbol = '~'
