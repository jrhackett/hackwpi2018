from server.src.point.point import Point
from server.src.map.resources import ResourceType


class BaseTile:
    """
    Base tile implementation that all tiles are derived from.  Tiles are passive objects and are interacted with; they
    do not cause interactions but instead respond to interactions.
    """
    point: Point
    quantity: int
    symbol: str
    resource_type: ResourceType
