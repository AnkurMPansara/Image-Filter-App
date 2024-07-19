from PyQt5.QtWidgets import QWidget, QHBoxLayout ,QVBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.layout = QHBoxLayout(self)
        self.left_section = LeftSection()
        self.right_section = RightSection()

        self.layout.addWidget(self.left_section, 3)
        self.layout.addWidget(self.right_section, 2)

        self.setLayout(self.layout)

class LeftSection(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        print("Called")
    
    def initUI(self):
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)
        self.preview = Preview()
        self.layout.addWidget(self.preview)

class RightSection(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)
        self.select_image = InputImage()
        self.layout.addWidget(self.select_image)

class Preview(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.label = QLabel("Preview")
        self.label.setAlignment(Qt.AlignLeft)
        self.layout.addWidget(self.label)

        self.image = QLabel()
        self.layout.addWidget(self.image)
        self.load_image(r"C:\Users\Imart\Downloads\7GEyP11-prince-of-persia-the-two-thrones-wallpaper.jpg")
    
    def load_image(self, path):
        pixmap = QPixmap(path)
        self.image.setPixmap(pixmap.scaled(self.image.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.image.setAlignment(Qt.AlignCenter)

class InputImage(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)
        
        self.select_button = QPushButton("Select Image", self)
        self.select_button.clicked.connect(self.select_image)
        self.layout.addWidget(self.select_button)
        self.input_image = QLabel("Preivew")
        self.input_image.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.input_image)
    
    def select_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)", options=options)
        if file_name:
            pixmap = QPixmap(file_name)
            self.input_image.setPixmap(pixmap)
            self.input_image.setScaledContents(True)