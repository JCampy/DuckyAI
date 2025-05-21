import os
from PyQt6.QtWidgets import QLabel, QMainWindow, QMenu, QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QAction

class RubberDuck(QMainWindow):

    def __init__(self, tts, model, spt):
        super().__init__()
        self.initUI()
        self.tts = tts
        self.model = model
        self.spt = spt

    def initUI(self):
        # Set window properties
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setGeometry(100, 100, 200, 200)

        # Load duck image
        image_path = os.path.join(os.path.dirname(__file__), 'assets', 'ducky one.png')
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap(image_path).scaled(
            150, 150,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
        self.label.setGeometry(25, 25, 150, 150)

        self.oldPos = None
        self.setupContextMenu()

    def setupContextMenu(self):
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)

    def showContextMenu(self, position):
        contextMenu = QMenu(self)
        
        # Add menu items
        exitAction = QAction("Exit", self)
        exitAction.triggered.connect(self.handle_exit)
        contextMenu.addAction(exitAction)
        
        contextMenu.exec(self.mapToGlobal(position))

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.oldPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self.oldPos is not None:
            delta = event.globalPosition().toPoint() - self.oldPos
            self.move(self.pos() + delta)
            self.oldPos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self.oldPos = None

    def handle_exit(self):
        print("Closing application")
        self.spt.update_run_condition()
        QApplication.instance().quit()