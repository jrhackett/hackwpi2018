from server.src.map import tiles
from server.src.map.resources import ResourceType
from server.src.map.tiles.tile_factory import TileFactory


class Map:
    """
    2x2 representation of the world in which the simulation will take place.
    """
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.tiles = [[None for _ in range(width)] for _ in range(height)]
        self.init_tiles()

    def init_tiles(self):
        """
        Initialize all of the map's tiles to be empty spaces
        :return:
        """
        for x in range(self.width):
            for y in range(self.height):
                new_tile = TileFactory.make_tile(ResourceType.NONE)
                new_tile.x = x
                new_tile.y = y
                self.tiles[x][y] = new_tile

    def get_tile(self, x: int, y: int) -> tiles.BaseTile:
        """
        Retrieves the tile at the given x and y location.  (Hides the internal representation of tiles.)
        :param x: x position of tile
        :param y: y position of tile
        :return: BaseTile object
        """
        if not self.is_valid_position(x, y):
            raise MapBoundsError(
                'Position <{}, {}> is outside of map bounds. Map is({}x{})'.format(x, y, self.width, self.height))
        return self.tiles[x][y]

    def set_tile(self, x: int, y: int, tile: tiles.BaseTile):
        """
        Sets the tile at the given x and y locations to be a new tile. (Hides the internal representation of tiles.)
        :param x: x position of tile
        :param y: y position of tile
        :param tile: BaseTile object
        :return:
        """
        if self.is_valid_position(x, y):
            self.tiles[x][y] = tile

    def is_valid_position(self, x: int, y: int) -> bool:
        """
        Returns true if the provided coordinates are a valid location on the map.
        :param x: x position of tile
        :param y: y position of tile
        :return:
        """
        return 0 <= x < self.width and 0 <= y < self.height

    def format_map_as_str(self) -> str:
        """
        Formats the map as a string, using each tiles symbol to represent the tile.  Does not display the resource count
        associated with each tile.s
        :return:
        """
        map_str = ""
        for x in range(self.width):
            for y in range(self.height):
                map_str += self.get_tile(x, y).symbol
            map_str += '\n'
        return map_str


class MapBoundsError(Exception):
    pass
