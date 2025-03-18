import sys
import random
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtCore import Qt, QTimer

class MouseTrackerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("F1D022108_Ajundasrika Anugrahanti TS")
        self.setGeometry(100, 100, 500, 400)
        
        self.label = QLabel("Move the mouse here!", self)
        self.label.setGeometry(200, 180, 150, 30)
        self.label.setStyleSheet("background-color: lightgray;")
        
        self.setMouseTracking(True)
        self.label.setMouseTracking(True)

        self.last_mouse_x = 200
        self.last_mouse_y = 180

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move_label_to_mouse)
        self.timer.start(700)  # 1 detik (1000 ms)
        
    def mouseMoveEvent(self, event):
        self.label.setText(f"X: {event.x()}, Y: {event.y()}")
       
        self.last_mouse_x = event.x()
        self.last_mouse_y = event.y()
    
    def enterEvent(self, event):
        x = random.randint(0, self.width() - self.label.width())
        y = random.randint(0, self.height() - self.label.height())
        self.label.move(x, y)

    def move_label_to_mouse(self):
        self.label.move(self.last_mouse_x, self.last_mouse_y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MouseTrackerApp()
    window.show()
    sys.exit(app.exec_())
