import pytest

from server.src.map import tiles
from server.src.map.resources import ResourceType


class TestTileClasses:

    @pytest.mark.parametrize('tile_class, expected_type, expected_symbol', [
        (tiles.CoalTile, ResourceType.COAL, '*'),
        (tiles.CopperTile, ResourceType.COPPER, 'C'),
        (tiles.FoodTile, ResourceType.FOOD, 'F'),
        (tiles.GoldTile, ResourceType.GOLD, 'G'),
        (tiles.IronTile, ResourceType.IRON, 'I'),
        (tiles.NoneTile, ResourceType.NONE, ' '),
        (tiles.OilTile, ResourceType.OIL, 'O'),
        (tiles.WaterTile, ResourceType.WATER, '~'),
        (tiles.WoodTile, ResourceType.WOOD, 'W')
    ])
    def test_tile_symbols_and_enumerations(self, tile_class, expected_type: ResourceType, expected_symbol: str):
        tile: tiles.BaseTile = tile_class()
        assert expected_type == tile.resource_type
        assert expected_symbol == tile.symbol
