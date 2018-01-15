from tornado import websocket, web, ioloop
from server.src.api.websockets.websocket_factory import WebsocketFactory
from server.src.api.websockets.websocket_topic import WebsocketTopic

game_engine_message_instance = []
tile_exhausted_instance = []
player_moved_instance = []


# For communicating with the game engine.  Currently only
# receives data, does not write.
class GameEngineMessageHandler(websocket.WebSocketHandler):
    def data_received(self, chunk):
        pass

    # Keep reference to instance to maintain singleton pattern.
    def open(self):
        if self not in game_engine_message_instance:
            game_engine_message_instance.append(self)

    # Called when game engine sends us message. Forward message to correct
    # socket handler.
    def on_message(self, message):
        for case in message.type:
            if case(WebsocketTopic.PLAYER_MOVED):
                player_moved_instance[0].send_update(message.data)
            if case(WebsocketTopic.TILE_EXHAUSTED):
                tile_exhausted_instance[0].send_update(message.data)
            if case():
                self.write_message(u"You said: " + message + " but you suck and I can't make any sense of it, sooo.")
                print(u"Bad emum type contained in message from game engine: " + message)

    def on_close(self):
        if self in game_engine_message_instance:
            game_engine_message_instance.remove(self)


app = web.Application([
    (r'/tile_exhausted_ws', WebsocketFactory.make_websocket(WebsocketTopic.TileExhaustedSocketHandler)),
    (r'/player_moved_ws', WebsocketFactory.make_websocket(WebsocketTopic.PlayerMovedSocketHandler)),
    (r'/game_engine_msg_ws', GameEngineMessageHandler)
])

if __name__ == '__main__':
    app.listen(8888)
    ioloop.IOLoop.instance().start()
