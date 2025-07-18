from minicad.commands.command import Command

from minicad.model.shape import Shape


class CreateShapeCommand(Command):
    def __init__(self, shape: Shape, shapes: list[Shape]):
        self._shapes = shapes
        self._shape = shape

    def execute(self) -> None:
        self._shapes.append(self._shape)

    def undo(self) -> None:
        self._shape = self._shapes.pop()

    def redo(self) -> None:
        self.execute()
