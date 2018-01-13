import pytest
from swarm_af_server.src.map import tiles
from swarm_af_server.src.map.tiles import impl
from swarm_af_server.src.map.resources import ResourceType


class TestTileClasses:

    @pytest.mark.parametrize('tile_class, expected_type, expected_symbol', [
        (impl.CoalTile, ResourceType.COAL, '*'),
        (impl.CopperTile, ResourceType.COPPER, 'C'),
        (impl.FoodTile, ResourceType.FOOD, 'F'),
        (impl.GoldTile, ResourceType.GOLD, 'G'),
        (impl.IronTile, ResourceType.IRON, 'I'),
        (impl.NoneTile, ResourceType.NONE, ' '),
        (impl.OilTile, ResourceType.OIL, 'O'),
        (impl.WaterTile, ResourceType.WATER, '~'),
        (impl.WoodTile, ResourceType.WOOD, 'W'),
    ])
    def test_tile_symbols_and_enumerations(self, tile_class, expected_type: ResourceType, expected_symbol: str):
        tile: tiles.BaseTile = tile_class()
        assert expected_type == tile.resource_type
        assert expected_symbol == tile.symbol
