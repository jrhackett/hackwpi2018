from swarm_af_server.src.map import tiles


class Map:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.tiles = [[None for _ in range(width)] for _ in range(height)]

    def init_tiles(self):
        for x in range(self.width):
            for y in range(self.height):
                new_tile = tiles.NoneTile()
                new_tile.x = x
                new_tile.y = y
                self.tiles[x][y] = new_tile

    def get_tile(self, x: int, y: int) -> tiles.BaseTile:
        if not self.is_valid_position(x, y):
            raise MapBoundsError(
                'Position <{}, {}> is outside of map bounds. Map is({}x{})'.format(x, y, self.width, self.height))
        return tiles[x][y]

    def is_valid_position(self, x: int, y: int):
        return 0 <= x < self.width and 0 <= y < self.height


class MapBoundsError(Exception):
    pass