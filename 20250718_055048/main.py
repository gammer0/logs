import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from logic.selector import select_random_topic
from data.graph_manager import GraphManager


class LearnMateApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('LearnMate')
        self.setGeometry(300, 300, 400, 200)

        self.layout = QVBoxLayout()
        self.label = QLabel('Welcome to LearnMate! Click the button to start learning.')
        self.layout.addWidget(self.label)

        self.button = QPushButton('Start Learning')
        self.button.clicked.connect(self.start_learning)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)
        self.graph = GraphManager('data/learning_map.json')

    def start_learning(self):
        topic = select_random_topic(self.graph.learning_map)
        if topic:
            self.label.setText(f'Learning about: {topic}')
        else:
            self.label.setText('No topics available to learn.')

def main():
    app = QApplication(sys.argv)
    window = LearnMateApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()