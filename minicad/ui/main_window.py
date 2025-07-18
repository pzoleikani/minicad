from functools import partial

from PySide6.QtWidgets import QMainWindow, QToolBar
from PySide6.QtGui import QPainter, QPaintEvent, QAction

from minicad.commands.command_stack import CommandStack

from minicad.model.shape import Shape

from minicad.ui.dialogs import ActionFactory


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.shapes: list[Shape] = []
        self.commandStack = CommandStack()

        self.initUI()

    def initUI(self) -> None:
        toolbar = QToolBar("Mini CAD Toolbar")
        self.addToolBar(toolbar)

        action_factory = ActionFactory()

        for name, create in action_factory.get_dialogs().items():
            action = QAction(name, self)
            create_func = partial(create, self.shapes, self.commandStack)
            action.triggered.connect(create_func)
            toolbar.addAction(action)

        undoAction = QAction("Undo", self)
        undoAction.triggered.connect(self.commandStack.undo)
        toolbar.addAction(undoAction)

        redoAction = QAction("Redo", self)
        redoAction.triggered.connect(self.commandStack.redo)
        toolbar.addAction(redoAction)

        self.resize(1000, 800)
        self.setWindowTitle("Mini CAD")
        self.show()

    def paintEvent(self, e: QPaintEvent) -> None:
        with QPainter(self) as painter:
            for shape in self.shapes:
                shape.draw(painter)
        self.update()
