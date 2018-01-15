from server.src.api.websockets import impl
from server.src.api.websockets.websocket_topic import WebsocketTopic


class WebsocketFactory:

    @staticmethod
    def make_websocket(websocket_topic: WebsocketTopic):
        if websocket_topic == WebsocketTopic.PLAYER_MOVED:
            return impl.PlayerMovedSocketHandler()
        if websocket_topic == WebsocketTopic.TILE_EXHAUSTED:
            return impl.TileExhaustedSocketHandler()
