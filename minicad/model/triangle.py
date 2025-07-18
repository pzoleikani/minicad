from minicad.model.shape import Shape
from minicad.model.point import Point

from PySide6.QtGui import QPainter
from PySide6.QtCore import QRectF, QPoint

import math


class Triangle(Shape):
    def __init__(self, center: Point, side: float):
        super().__init__(center)
        self._side = side

    # TODO: Task 4 - Implement the scale method

    def draw(self, painter: QPainter) -> None:
        # TODO: Task 3 - Implement the drawing mechanism for a triangle
        pass
