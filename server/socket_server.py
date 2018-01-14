from tornado import websocket, web, ioloop
from enum import Enum
import json

game_engine_message_instance = []
tile_exhausted_instance = []
player_moved_instance = []

# To support new message types, add to this enum.
# Each enum type has a corresponding handler class, below.
class MessageTypes(Enum):
    TILE_EXHAUSTED = "tile_exhausted"
    PLAYER_MOVED = "player_moved"

# For communicating with the game engine.  Currently only
# receives data, does not write.
class GameEngineMessageHandler(websocket.WebSocketHandler):
    # Keep reference to instance to maintain singleton pattern.
    def open(self):
        if self not in game_engine_message_instance:
            game_engine_message_instance.append(self)
    # Called when game engine sends us message. Forward message to correct
    # socket handler.
    def on_message(self, message):
        for case in message.type:
            if case(MessageTypes.PLAYER_MOVED):
                player_moved_instance[0].send_update(message.data)
            if case(MessageTypes.TILE_EXHAUSTED):
                tile_exhausted_instance[0].send_update(message.data)
            if case():
                self.write_message(u"You said: " + message + " but you suck and I can't make any sense of it, sooo.")
                print(u"Bad emum type contained in message from game engine: " + message)

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