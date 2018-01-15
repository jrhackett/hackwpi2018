from tornado import web, ioloop
from server.src.api.websockets.websocket_factory import WebsocketFactory
from server.src.api.websockets.websocket_topic import WebsocketTopic

app = web.Application([
    (r'/tile_exhausted_ws', WebsocketFactory.make_websocket(WebsocketTopic.TileExhaustedSocketHandler)),
    (r'/player_moved_ws', WebsocketFactory.make_websocket(WebsocketTopic.PlayerMovedSocketHandler))
])

if __name__ == '__main__':
    app.listen(8888)
    ioloop.IOLoop.instance().start()
