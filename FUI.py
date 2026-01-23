import sys
import psutil
import datetime
import threading
import json
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QLabel, QFrame, 
                             QStackedWidget, QLineEdit, QMessageBox, QProgressBar)
from PyQt6.QtCore import QTimer, Qt, QThread, pyqtSignal
from PyQt6.QtGui import QFont, QColor, QPalette

# Import your Governance Tool (ensure governance_tool.py is in the same folder)
try:
    import governance_tool
    GOVERNANCE_ACTIVE = True
except ImportError:
    GOVERNANCE_ACTIVE = False
    print("⚠️ Governance Tool not found. Blockchain features disabled.")

# --- THEME & CONFIG ---
FROST_BLUE = "#00e5ff"
FROST_DARK = "#121212"
FONT_MAIN = "Courier New" # Hacker/Terminal style

class SystemMonitor(QThread):
    stats_signal = pyqtSignal(float, float)

    def run(self):
        while True:
            cpu = psutil.cpu_percent(interval=1)
            ram = psutil.virtual_memory().percent
            self.stats_signal.emit(cpu, ram)

class FUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FOME // Finux Operating Environment")
        self.setGeometry(100, 100, 1280, 720)
        # self.showFullScreen() # Uncomment for actual OS mode

        self.apply_theme()
        
        # Main Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # 1. Sidebar (Launcher)
        self.create_sidebar()

        # 2. Main Content Area (Stack)
        self.content_stack = QStackedWidget()
        self.main_layout.addWidget(self.content_stack)

        # 3. Initialize Pages
        self.page_dashboard = self.create_dashboard()
        self.page_terminal = self.create_terminal_view()
        self.page_governance = self.create_governance_view()

        self.content_stack.addWidget(self.page_dashboard)
        self.content_stack.addWidget(self.page_terminal)
        self.content_stack.addWidget(self.page_governance)

        # Start System Monitor
        self.monitor = SystemMonitor()
        self.monitor.stats_signal.connect(self.update_stats)
        self.monitor.start()

    def apply_theme(self):
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(FROST_DARK))
        palette.setColor(QPalette.ColorRole.WindowText, QColor("white"))
        self.setPalette(palette)
        self.setStyleSheet(f"""
            QMainWindow {{ background-color: {FROST_DARK}; }}
            QLabel {{ color: white; font-family: '{FONT_MAIN}'; }}
            QPushButton {{ 
                background-color: #1e1e1e; 
                color: {FROST_BLUE}; 
                border: 1px solid {FROST_BLUE}; 
                padding: 10px;
                font-family: '{FONT_MAIN}';
                font-weight: bold;
            }}
            QPushButton:hover {{ background-color: {FROST_BLUE}; color: black; }}
            QLineEdit {{ 
                background-color: #333; color: white; border: 1px solid #555; padding: 5px; 
                font-family: '{FONT_MAIN}';
            }}
        """)

    def create_sidebar(self):
        sidebar = QFrame()
        sidebar.setFixedWidth(200)
        sidebar.setStyleSheet("background-color: #0a0a0a; border-right: 1px solid #333;")
        layout = QVBoxLayout(sidebar)
        
        # Logo / Header
        lbl_logo = QLabel("FOME\n[v0.1]")
        lbl_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl_logo.setStyleSheet(f"font-size: 24px; color: {FROST_BLUE}; margin-bottom: 20px;")
        layout.addWidget(lbl_logo)

        # Nav Buttons
        btn_dash = QPushButton("DASHBOARD")
        btn_dash.clicked.connect(lambda: self.content_stack.setCurrentWidget(self.page_dashboard))
        layout.addWidget(btn_dash)

        btn_gov = QPushButton("PROTOCOL GOV")
        btn_gov.clicked.connect(lambda: self.content_stack.setCurrentWidget(self.page_governance))
        layout.addWidget(btn_gov)

        btn_term = QPushButton("TERMINAL")
        btn_term.clicked.connect(lambda: self.content_stack.setCurrentWidget(self.page_terminal))
        layout.addWidget(btn_term)

        layout.addStretch()
        
        # System Stats (Tiny)
        self.lbl_cpu = QLabel("CPU: 0%")
        self.lbl_ram = QLabel("RAM: 0%")
        layout.addWidget(self.lbl_cpu)
        layout.addWidget(self.lbl_ram)

        # Clock
        self.lbl_time = QLabel("00:00:00")
        self.lbl_time.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_time.setStyleSheet("font-size: 16px; margin-top: 10px;")
        layout.addWidget(self.lbl_time)
        
        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)

        self.main_layout.addWidget(sidebar)

    def create_dashboard(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        
        lbl_welcome = QLabel("SYSTEM READY")
        lbl_welcome.setStyleSheet("font-size: 48px; color: #555;")
        lbl_welcome.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(lbl_welcome)
        
        # Placeholder for graphical modules
        return page

    def create_terminal_view(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        lbl = QLabel("FINUX SHELL ACCESS [RESTRICTED]")
        layout.addWidget(lbl)
        
        term_output = QLabel("> Initializing Frost Kernel...\n> Connection established.\n> Awaiting input...")
        term_output.setStyleSheet("background-color: black; color: #0f0; padding: 20px; font-family: 'Courier New';")
        term_output.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(term_output, 1)
        
        cmd_input = QLineEdit()
        cmd_input.setPlaceholderText("Enter command...")
        layout.addWidget(cmd_input)
        
        return page

    def create_governance_view(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        
        header = QLabel("FROST PROTOCOL GOVERNANCE")
        header.setStyleSheet(f"font-size: 24px; color: {FROST_BLUE};")
        layout.addWidget(header)

        if not GOVERNANCE_ACTIVE:
            layout.addWidget(QLabel("Error: governance_tool.py not linked."))
            return page

        # Governance Controls
        self.gov_output = QLabel("Status: Idle")
        self.gov_output.setStyleSheet("border: 1px solid #333; padding: 10px;")
        layout.addWidget(self.gov_output)

        # Vote Section
        btn_check = QPushButton("Check Latest Proposal")
        btn_check.clicked.connect(self.check_proposal)
        layout.addWidget(btn_check)

        vote_layout = QHBoxLayout()
        btn_yes = QPushButton("VOTE YES (Support)")
        btn_yes.clicked.connect(lambda: self.cast_vote(True))
        btn_no = QPushButton("VOTE NO (Reject)")
        btn_no.clicked.connect(lambda: self.cast_vote(False))
        
        vote_layout.addWidget(btn_yes)
        vote_layout.addWidget(btn_no)
        layout.addLayout(vote_layout)

        layout.addStretch()
        return page

    # --- LOGIC ---
    def update_time(self):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        self.lbl_time.setText(now)

    def update_stats(self, cpu, ram):
        self.lbl_cpu.setText(f"CPU: {cpu}%")
        self.lbl_ram.setText(f"RAM: {ram}%")

    def check_proposal(self):
        # This calls the script we wrote earlier
        if GOVERNANCE_ACTIVE:
            try:
                # Mocking the read for UI responsiveness (Replace with actual call)
                self.gov_output.setText("Fetching data from Base Mainnet...\n(Simulated) Proposal #1: 'Increase Block Size'\nVotes For: 55%\nVotes Against: 45%")
            except Exception as e:
                self.gov_output.setText(f"Error: {e}")

    def cast_vote(self, support):
        if GOVERNANCE_ACTIVE:
            vote_str = "YES" if support else "NO"
            # Here you would call governance_tool.vote(1, support)
            QMessageBox.information(self, "Vote Submitted", f"Casting {vote_str} with Lead Dev Weight (5%).\n\nCheck terminal for TX Hash.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FUI()
    window.show()
    sys.exit(app.exec())
