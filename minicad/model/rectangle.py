from minicad.model.shape import Shape
from minicad.model.point import Point

from PySide6.QtGui import QPainter
from PySide6.QtCore import QRectF


class Rectangle(Shape):
    def __init__(self, center: Point, width: float, height: float):
        super().__init__(center)
        self._width = width
        self._height = height

    # TODO: Task 4 - Implement the scale method

    def draw(self, painter: QPainter) -> None:
        rect = QRectF(
            self._center.x - (self._width / 2.0),
            self._center.y - (self._height / 2.0),
            self._width,
            self._height,
        )
        painter.drawRect(rect)

        painter.drawText(self._center.x, self._center.y, str(self._id))
