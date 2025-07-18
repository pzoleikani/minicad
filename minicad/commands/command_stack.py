from minicad.commands.command import Command


class CommandStack:
    def __init__(self) -> None:
        self.undoStack: list[Command] = []
        self.redoStack: list[Command] = []

    def execute(self, command: Command) -> None:
        # TODO: Task 5 - Implement the command stack
        command.execute()
        # ...

    def undo(self) -> None:
        # TODO: Task 5 - Implement the command stack
        pass

    def redo(self) -> None:
        # TODO: Task 5 - Implement the command stack
        pass
