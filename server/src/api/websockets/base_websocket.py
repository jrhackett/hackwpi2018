from tornado import websocket

base_instance = []


class BaseSocketHandler(websocket.WebSocketHandler):
    def data_received(self, chunk):
        pass

    def check_origin(self, origin):
        return True

    def open(self):
        if self not in base_instance:
            base_instance.append(self)

    def on_message(self, message):
        self.write_message(u"You said: " + message)
        print(u"You said: " + message)

    def send_update(self, update_text):
        self.write_message(update_text)

    def on_close(self):
        if self in base_instance:
            base_instance.remove(self)
