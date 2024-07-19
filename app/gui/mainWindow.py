from PyQt5.QtWidgets import QMainWindow
from app.gui.widgets import MainWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Filter Forge")
        self.showMaximized()
        self.initUI()

    def initUI(self):
        self.master_widget = MainWidget()
        self.setCentralWidget(self.master_widget)
