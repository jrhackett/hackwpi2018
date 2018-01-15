from server.src.point.point import Point
from server.src.map.resources import ResourceType


class BaseTile:

    point: Point
    quantity: int
    symbol: str
    resource_type: ResourceType
