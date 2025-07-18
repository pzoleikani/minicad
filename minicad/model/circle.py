from minicad.model.shape import Shape
from minicad.model.point import Point

from PySide6.QtGui import QPainter


class Circle(Shape):
    def __init__(self, center: Point, radius: float):
        super().__init__(center)
        self._radius = radius

    # TODO: Task 4 - Implement the scale method

    def draw(self, painter: QPainter) -> None:
        topLeftX = int(self._center.x - self._radius)
        topLeftY = int(self._center.y - self._radius)
        painter.drawEllipse(
            topLeftX, topLeftY, int(self._radius * 2), int(self._radius * 2)
        )

        painter.drawText(self._center.x, self._center.y, str(self._id))
