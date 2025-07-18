from abc import ABC, abstractmethod
from minicad.model.point import Point

from PySide6.QtGui import QPainter


class Shape(ABC):
    counter: int = 0

    def __init__(self, center: Point):
        self._center = center
        self._id = Shape.counter
        Shape.counter += 1

    @abstractmethod
    def draw(self, painter: QPainter) -> None:
        raise NotImplementedError

    # TODO: Task 4 - Implement the scale method

    def translate(self, dx: int, dy: int) -> None:
        self._center.translate(dx, dy)
