import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QLineEdit, QMessageBox
)
from PyQt6.QtGui import QIcon

from logic.github_upload import upload_file_to_github

class SourceUploadUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("文件上传")
        self.setWindowIcon(QIcon("icon.png"))
        self.setFixedSize(400, 200)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("请选择要上传的文件：")
        self.layout.addWidget(self.label)

        self.file_path_input = QLineEdit()
        self.file_path_input.setReadOnly(True)
        self.layout.addWidget(self.file_path_input)


        self.upload_button = QPushButton("上传")
        self.upload_button.clicked.connect(upload_file_to_github)
        self.layout.addWidget(self.upload_button)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SourceUploadUI()
    window.show()
    sys.exit(app.exec())