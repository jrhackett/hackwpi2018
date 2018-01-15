from server.src.api.websockets.base_websocket import BaseSocketHandler
from server.src.api.websockets.websocket_topic import WebsocketTopic

player_moved_instance = []


class PlayerMovedSocketHandler(BaseSocketHandler):
    topic: WebsocketTopic = WebsocketTopic.PLAYER_MOVED
