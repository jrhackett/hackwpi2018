from tornado import websocket, web, ioloop
from enum import Enum
import json

game_engine_message_instance = []
tile_exhausted_instance = []
player_moved_instance = []

class MessageTypes(Enum):
    TILE_EXHAUSTED = "tile_exhausted"
    PLAYER_MOVED = "player_moved"

class GameEngineMessageHandler(websocket.WebSocketHandler):
    def open(self):
        if self not in game_engine_message_instance:
            game_engine_message_instance.append(self)

    def on_message(self, message):
        for case in message.type:
            if case(MessageTypes.PLAYER_MOVED):
                player_moved_instance[0].send_update(message.data)
            if case(MessageTypes.TILE_EXHAUSTED):
                tile_exhausted_instance[0].send_update(message.data)
        self.write_message(u"You said: " + message)
        print(u"You said: " + message)

    def on_close(self):
        if self in game_engine_message_instance:
            game_engine_message_instance.remove(self)

class TileExhaustedSocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        if self not in tile_exhausted_instance:
            tile_exhausted_instance.append(self)

    def on_message(self, message):
        self.write_message(u"You said: " + message)
        print(u"You said: " + message)

    def send_update(self, update_text):
        self.write_message(update_text)

    def on_close(self):
        if self in tile_exhausted_instance:
            tile_exhausted_instance.remove(self)

class PlayerMovedSocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def send_update(self, update_text):
        self.write_message(update_text)

    def open(self):
        if self not in player_moved_instance:
            player_moved_instance.append(self)

    def on_message(self, message):
        self.write_message(u"You said: " + message)
        print(u"You said: " + message)

    def on_close(self):
        if self in player_moved_instance:
            player_moved_instance.remove(self)



app = web.Application([
    (r'/tile_exhausted_ws', TileExhaustedSocketHandler),
    (r'/player_moved_ws', PlayerMovedSocketHandler),
    (r'/game_engine_msg_ws', GameEngineMessageHandler)
])

if __name__ == '__main__':
    app.listen(8888)
    ioloop.IOLoop.instance().start()