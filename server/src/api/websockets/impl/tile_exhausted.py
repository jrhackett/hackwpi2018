from server.src.api.websockets.base_websocket import BaseSocketHandler
from server.src.api.websockets.websocket_topic import WebsocketTopic

tile_exhausted_instance = []


class TileExhaustedSocketHandler(BaseSocketHandler):
    topic: WebsocketTopic = WebsocketTopic.TILE_EXHAUSTED
