class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def translate(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy