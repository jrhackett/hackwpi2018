from swarm_af_server.src.map.resources import ResourceType


class BaseTile:

    x: int
    y: int
    quantity: int
    symbol: str
    resource_type: ResourceType
