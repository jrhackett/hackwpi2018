from server.src.api.websockets.base_websocket import BaseSocketHandler
from server.src.api.websockets.websocket_topic import WebsocketTopic

player_moved_instance = []


class PlayerMovedSocketHandler(BaseSocketHandler):
    def __init__(self):
        super.__init__()
        self.topic = WebsocketTopic.PLAYER_MOVED
