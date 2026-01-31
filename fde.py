# FDE: FROST DESKTOP ENVIRONMENT (KDE-Based)
# Engine: PyQt5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QListWidget, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor

class FDEPlasmaShell(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FDE Plasma Shell")
        self.setGeometry(100, 100, 1280, 720)

        # 1. The "Plasma" Style (Dark, Glassy)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(20, 20, 30))
        palette.setColor(QPalette.WindowText, QColor(0, 255, 255))
        self.setPalette(palette)

        # 2. The Bottom Panel (Taskbar)
        self.panel = QDockWidget("Frost Panel", self)
        self.panel.setAllowedAreas(Qt.BottomDockWidgetArea)
        self.panel.setFeatures(QDockWidget.NoDockWidgetFeatures) # Locked
        
        # Panel Content
        panel_widget = QWidget()
        panel_widget.setStyleSheet("background-color: #0f0f15; border-top: 2px solid #00ffff;")
        layout = QVBoxLayout()
        lbl = QLabel("❄️  Start  |  Finux Terminal  |  FrostMart  |  System Settings")
        lbl.setStyleSheet("color: cyan; font-weight: bold; padding: 10px;")
        layout.addWidget(lbl)
        panel_widget.setLayout(layout)
        
        self.panel.setWidget(panel_widget)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.panel)

        # 3. The Desktop Space (Widgets)
        self.desktop = QLabel("FDE WORKSPACE\n[Right Click to Add Widgets]", self)
        self.desktop.setAlignment(Qt.AlignCenter)
        self.desktop.setStyleSheet("font-size: 24px; color: #444;")
        self.setCentralWidget(self.desktop)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    shell = FDEPlasmaShell()
    shell.show()
    sys.exit(app.exec_())
