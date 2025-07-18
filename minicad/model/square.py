from minicad.model.shape import Shape
from minicad.model.point import Point

from PySide6.QtGui import QPainter
from PySide6.QtCore import QRectF


class Square(Shape):
    def __init__(self, center: Point, side: float):
        super().__init__(center)
        self._side = side

    # TODO: Task 4 - Implement the scale method

    def draw(self, painter: QPainter) -> None:
        rect = QRectF(
            self._center.x - (self._side / 2.0),
            self._center.y - (self._side / 2.0),
            self._side,
            self._side,
        )
        painter.drawRect(rect)

        painter.drawText(self._center.x, self._center.y, str(self._id))
