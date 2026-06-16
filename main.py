import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bintulu News AI")
        self.resize(400, 200)

        layout = QVBoxLayout()
        label = QLabel("Bintulu News AI Running")
        layout.addWidget(label)

        self.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
