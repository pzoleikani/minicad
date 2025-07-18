from minicad.commands.command import Command

from minicad.model.circle import Circle
from minicad.model.point import Point
from minicad.model.shape import Shape


class TranslateShapeCommand(Command):
    def __init__(self, shape: Shape, delta_x: int, delta_y: int):
        self._shape = shape
        self._delta_x = delta_x
        self._delta_y = delta_y

    def execute(self) -> None:
        self._shape.translate(self._delta_x, self._delta_y)

    def undo(self) -> None:
        self._shape.translate(-self._delta_x, -self._delta_y)

    def redo(self) -> None:
        self.execute()
