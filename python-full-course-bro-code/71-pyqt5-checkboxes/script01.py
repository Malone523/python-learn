import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 500, 500)
        self.checkbox = QCheckBox("tralala", self)

        self.initUI()


    def initUI(self):
        self.checkbox.setGeometry(10, 0, 500, 100)
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family: Arial;")
        self.checkbox.setChecked(False)

        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        if state == Qt.Checked:
            print("Yah")
        else:
            print("Nah")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()