from enum import Enum


class WebsocketTopic(Enum):
    TILE_EXHAUSTED = "tile_exhausted"
    PLAYER_MOVED = "player_moved"
