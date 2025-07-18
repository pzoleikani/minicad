from minicad.commands.command import Command

from minicad.model.shape import Shape


class ClearShapeCommand(Command):
    def __init__(self, index: int, shapes: list[Shape]):
        self._shapes = shapes
        self._index = index

    def execute(self) -> None:
        self._shape = self._shapes.pop(self._index)

    def undo(self) -> None:
        self._shapes.append(self._shape)

    def redo(self) -> None:
        self.execute()
