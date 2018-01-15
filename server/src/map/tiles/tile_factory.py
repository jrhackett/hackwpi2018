from server.src.map.tiles import impl
from server.src.map.resources import ResourceType


class TileFactory:
    """
    Factory to create new tiles.  Tiles should always be created via the TileFactory and never directly from their
    __init__ methods.
    """
    @staticmethod
    def make_tile(resource_type: ResourceType):
        if resource_type == ResourceType.COAL:
            return impl.CoalTile()
        if resource_type == ResourceType.COPPER:
            return impl.CopperTile()
        if resource_type == ResourceType.FOOD:
            return impl.FoodTile()
        if resource_type == ResourceType.GOLD:
            return impl.GoldTile()
        if resource_type == ResourceType.IRON:
            return impl.IronTile()
        if resource_type == ResourceType.NONE:
            return impl.NoneTile()
        if resource_type == ResourceType.OIL:
            return impl.OilTile()
        if resource_type == ResourceType.WATER:
            return impl.WaterTile()
        if resource_type == ResourceType.WOOD:
            return impl.WoodTile()
