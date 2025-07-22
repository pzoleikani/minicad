from minicad.commands.command import Command


class CommandStack:
    def __init__(self) -> None:
        self.undoStack: list[Command] = []
        self.redoStack: list[Command] = []

    def execute(self, command: Command) -> None:
        command.execute()
        self.undoStack.append(command)
        self.redoStack.clear()

    def undo(self) -> None:
        if self.undoStack:
            command = self.undoStack.pop()
            command.undo()
            self.redoStack.append(command)

    def redo(self) -> None:
        if self.redoStack:
            command = self.redoStack.pop()
            command.execute()
            self.undoStack.append(command)
