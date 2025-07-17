import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,QLabel, 
    QLineEdit, QPushButton, QCheckBox, QFrame
)
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QFont, QIcon, QPalette, QColor

from config.login import dump_news 

class LoginUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("loginUI")
        self.setWindowIcon(QIcon("icon.png"))  # 建议使用SVG图标
        self.setFixedSize(400, 500)

        
        # 主布局
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        
        # 初始化UI
        self.init_ui()
        self.setStyleSheet("""
                QWidget {
                    background: #f0f4fa;
                }
                QFrame {
                    background: #ffffff;
                    border: 1px solid #e0e0e0;
                    border-radius: 8px;
                    padding: 20px;
                }
                QLineEdit {
                    background: #f9f9f9;
                    border: 1px solid #ddd;
                    padding: 10px;
                    border-radius: 4px;
                }
                QPushButton {
                    background: qlineargradient(
                        x1:0, y1:0, x2:1, y2:0,
                        stop:0 #0088ff, stop:1 #00aaff
                    );
                    color: white;
                    padding: 12px;
                    border-radius: 6px;
                    font-weight: bold;
                }
                QCheckBox::indicator {
                    width: 16px;
                    height: 16px;
                }
            """)

    def init_ui(self):
        """构建所有UI组件"""
        
        # 标题
        self.title = QLabel("欢迎登录")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_font = QFont("Microsoft YaHei", 18, QFont.Weight.Bold)
        self.title.setFont(title_font)
        
        # 输入框容器
        input_frame = QFrame()
        input_frame.setFrameShape(QFrame.Shape.StyledPanel)
        
        # 用户名输入
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("github email")
        self.username_input.setClearButtonEnabled(True)
        
        # 密码输入
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setClearButtonEnabled(True)
        
        # 显示密码复选框
        self.show_password = QCheckBox("显示密码")
        self.show_password.toggled.connect(
            lambda: self.password_input.setEchoMode(
                QLineEdit.EchoMode.Normal if self.show_password.isChecked() 
                else QLineEdit.EchoMode.Password
            )
        )
        
        # 记住我选项
        self.remember_me = QCheckBox("保持登录状态")
        
        # 登录按钮
        self.login_btn = QPushButton("login")
        self.login_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.login_btn.clicked.connect(
            lambda: dump_news(
                self.username_input.text(), 
                self.password_input.text()
            )
        )
        
        
        # 布局组装
        input_layout = QVBoxLayout(input_frame)
        input_layout.addWidget(self.username_input)
        input_layout.addWidget(self.password_input)
        input_layout.addWidget(self.show_password)
        input_layout.addWidget(self.remember_me)
        input_layout.addSpacing(20)
        input_layout.addWidget(self.login_btn)
        
        # 主布局添加组件
        self.main_layout.addWidget(self.title)
        self.main_layout.addSpacing(30)
        self.main_layout.addWidget(input_frame)
        self.main_layout.addStretch(1)
        
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # 设置全局字体
    font = QFont("Segoe UI", 10)
    app.setFont(font)
    
    window = LoginUI()
    window.show()
    sys.exit(app.exec())