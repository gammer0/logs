import sys
import os
import json
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QCheckBox, QFrame, QTreeWidget, QTreeWidgetItem, QFileDialog
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon

from data.graph_manager import GraphManager
GraphManager(os.path.join(os.getcwd(), "data", "learning_map.json"))

class MapManagerUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Map Manager")
        self.setWindowIcon(QIcon("icon.png"))
        self.setFixedSize(600, 400)

        # 主布局
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # 树形控件
        self.tree = QTreeWidget()
        self.main_layout.addWidget(self.tree)

        # 加载按钮
        self.load_button = QPushButton("加载JSON文件")
        self.load_button.clicked.connect(self.load_json)
        self.main_layout.addWidget(self.load_button)

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
        
        
        # 输入框
        self.map_parentname_label = QLabel("父节点：")
        self.map_parentname_input = QLineEdit()
        self.map_childname_label = QLabel("子节点：")
        self.map_childname_input = QLineEdit()
        
        # 按钮
        self.add_button = QPushButton("添加节点")
        self.remove_button = QPushButton("删除节点")
    
        self.add_button.clicked.connect(
            lambda: GraphManager.add_child(
                self.map_parentname_input.text(),
                self.map_childname_input.text(),
            )
        )
        self.add_button.clicked.connect(self.load_json)
        self.remove_button.clicked.connect(
            lambda: GraphManager.remove_child(
                self.map_parentname_input.text(),
                self.map_childname_input.text(),
            )
        )
        self.remove_button.clicked.connect(self.load_json)

        
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.map_parentname_label)
        input_layout.addWidget(self.map_parentname_input)
        input_layout.addWidget(self.map_childname_label)
        input_layout.addWidget(self.map_childname_input)

        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.remove_button)
        
        # 将输入框和按钮布局添加到主布局
        self.main_layout.addLayout(input_layout)
        self.main_layout.addLayout(button_layout)

    def load_json(self):
        path = os.path.join(os.getcwd(),"data", "learning_map.json")
        if path:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.tree.clear()
            self.add_items(self.tree.invisibleRootItem(), data)

    def add_items(self, parent, node):
        item = QTreeWidgetItem([node.get("name", "无名节点")])
        parent.addChild(item)
        for child in node.get("children", []):
            self.add_items(item, child)

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapManagerUI()
    window.show()
    sys.exit(app.exec())