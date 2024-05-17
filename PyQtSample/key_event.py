import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel


class KeyEventSample(QWidget):

    def __init__(self, parent=None):
        super(KeyEventSample, self).__init__()
        self.initUI()
        # self.setWindowIcon(QtGui.QIcon('')) # 设置图标
        self.setWindowTitle("PyQt5 按键事件示例")  # 设置标题
        # self.setStyleSheet('background-color:rgb(84,82,119)') # 设置样式
        self.resize(800, 600)
        pass

    def initUI(self):
        mainLayout = QVBoxLayout()
        self.label = QLabel("TEST")
        self.label.move(10, 10)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        mainLayout.addWidget(self.label)

        self.setLayout(mainLayout)

    def keyPressEvent(self, a0: QtGui.QKeyEvent | None) -> None:
        if a0.key() == Qt.Key_Home:
            self.label.setText("Key HOME pressed")
            print("Key Home pressed")

        if a0.key() == Qt.Key_End:
            self.label.setText("Key END pressed")
            print("Key End pressed")

        if a0.key() == Qt.Key_Escape:
            self.label.setText("Key ESC pressed")
            print("Key Esc pressed")

        if a0.key() == Qt.Key_S:
            if a0.modifiers() & Qt.ControlModifier:
                self.label.setText("Key Ctrl+S pressed")
                print("Key Ctrl+S pressed")
            if a0.modifiers() & Qt.ShiftModifier:
                self.label.setText("Key Shift+S pressed")
                print("Key Shift+S pressed")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KeyEventSample()
    window.show()
    sys.exit(app.exec())
