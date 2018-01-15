
class Point:
    x: int = 0
    y: int = 0

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def set_point(self, x: int, y: int):
        self.x = x
        self.y = y
