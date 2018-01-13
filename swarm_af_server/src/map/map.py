from swarm_af_server.src.map import tiles
from swarm_af_server.src.map.tiles import impl


class Map:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.tiles = [[None for _ in range(width)] for _ in range(height)]
        self.init_tiles()

    def init_tiles(self):
        for x in range(self.width):
            for y in range(self.height):
                new_tile = impl.NoneTile()
                new_tile.x = x
                new_tile.y = y
                self.tiles[x][y] = new_tile

    def get_tile(self, x: int, y: int) -> tiles.BaseTile:
        if not self.is_valid_position(x, y):
            raise MapBoundsError(
                'Position <{}, {}> is outside of map bounds. Map is({}x{})'.format(x, y, self.width, self.height))
        return self.tiles[x][y]

    def set_tile(self, x: int, y: int, tile: tiles.BaseTile):
        if self.is_valid_position(x, y):
            self.tiles[x][y] = tile

    def is_valid_position(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def format_map_as_str(self) -> str:
        map_str = ""
        for x in range(self.width):
            for y in range(self.height):
                map_str += self.get_tile(x, y).symbol
            map_str += '\n'
        return map_str


class MapBoundsError(Exception):
    pass
