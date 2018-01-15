
class Point:
    x: int = 0
    y: int = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_point(self):
        return self.x, self.y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_point(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y
