from server.src.api.websockets.base_websocket import BaseSocketHandler
from server.src.api.websockets.websocket_topic import WebsocketTopic

tile_exhausted_instance = []


class TileExhaustedSocketHandler(BaseSocketHandler):
    def __init__(self):
        self.topic = WebsocketTopic.PLAYER_MOVED
