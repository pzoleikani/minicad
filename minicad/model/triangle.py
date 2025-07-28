from minicad.model.shape import Shape
from minicad.model.point import Point

from PySide6.QtGui import QPainter
from PySide6.QtCore import QRectF, QPoint

import math


class Triangle(Shape):
    def __init__(self, center: Point, side: float):
        super().__init__(center)
        self._side = side

    # Task 4 - Implement the scale method
    def scale(self, factor: float) -> None:
        self._side *= factor

    # Task 3 - Implement the drawing mechanism for a triangle
    def draw(self, painter: QPainter) -> None:
        x = self._center.x
        y = self._center.y
        side = self._side

        h = (math.sqrt(3) / 2) * side
        half = side / 2

        p1 = QPoint(x, y - (2 / 3) * h)
        p2 = QPoint(x - half, y + (1 / 3) * h)
        p3 = QPoint(x + half, y + (1 / 3) * h)

        painter.drawPolygon([p1, p2, p3])

