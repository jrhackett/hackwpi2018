from tornado import websocket, web, ioloop
import json

cl = []


class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        if self not in cl:
            cl.append(self)
            i = 0
            while i < 10:
                self.write_message(u"hiii  ")
                i = i + 1

    def on_message(self, message):
        self.write_message(u"You said: " + message)
        print(u"You said: " + message)

    def on_close(self):
        if self in cl:
            cl.remove(self)


app = web.Application([
    (r'/ws', SocketHandler),
])

if __name__ == '__main__':
    app.listen(8888)
    ioloop.IOLoop.instance().start()