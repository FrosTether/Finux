import sys
import psutil
import datetime
import csv
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QLabel, QFrame, 
                             QStackedWidget, QLineEdit, QMessageBox)
from PyQt6.QtCore import QTimer, Qt, QThread, pyqtSignal
from PyQt6.QtGui import QColor, QPalette

# Import your tools
try:
    import governance_tool
    GOVERNANCE_ACTIVE = True
except ImportError:
    GOVERNANCE_ACTIVE = False

# --- CONFIGURATION ---
FROST_BLUE = "#00e5ff"
FROST_RED = "#ff3333"
FROST_DARK = "#121212"
FONT_MAIN = "Courier New"
LEDGER_FILE = "finux_ledger.csv"

# --- WORKER THREADS ---
class VoteWorker(QThread):
    finished = pyqtSignal(dict)
    def __init__(self, pid, support):
        super().__init__()
        self.pid = pid
        self.support = support
    def run(self):
        if GOVERNANCE_ACTIVE:
            result = governance_tool.vote_on_blockchain(self.pid, self.support)
            self.finished.emit(result)
        else:
            self.finished.emit({"status": "error", "message": "Governance tool missing"})

class DataFetcher(QThread):
    data_ready = pyqtSignal(dict)
    def run(self):
        if GOVERNANCE_ACTIVE:
            data = governance_tool.get_latest_proposal()
            self.data_ready.emit(data)

# --- MAIN UI ---
class FUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FOME // Finux Operating Environment")
        self.setGeometry(100, 100, 1280, 720)
        self.apply_theme()
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.create_sidebar()
        
        self.content_stack = QStackedWidget()
        self.main_layout.addWidget(self.content_stack)
        
        # Initialize Pages
        self.page_dashboard = self.create_dashboard()
        self.page_gov = self.create_governance_view()
        self.page_terminal = self.create_terminal_view()
        
        self.content_stack.addWidget(self.page_dashboard)
        self.content_stack.addWidget(self.page_gov)
        self.content_stack.addWidget(self.page_terminal)
        
        # Auto-refresh Ledger on Dashboard load
        self.update_financials()

    def apply_theme(self):
        self.setStyleSheet(f"background-color: {FROST_DARK}; color: white; font-family: '{FONT_MAIN}';")

    def create_sidebar(self):
        sidebar = QFrame()
        sidebar.setFixedWidth(220)
        sidebar.setStyleSheet("background-color: #0a0a0a; border-right: 1px solid #333;")
        layout = QVBoxLayout(sidebar)
        
        lbl = QLabel("FOME v1.1")
        lbl.setStyleSheet(f"color: {FROST_BLUE}; font-size: 24px; font-weight: bold; margin-bottom: 20px;")
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(lbl)
        
        # Navigation
        btn_dash = QPushButton("DASHBOARD")
        btn_dash.clicked.connect(lambda: self.content_stack.setCurrentWidget(self.page_dashboard))
        self.style_nav_btn(btn_dash)
        layout.addWidget(btn_dash)

        btn_gov = QPushButton("GOVERNANCE")
        btn_gov.clicked.connect(lambda: self.content_stack.setCurrentWidget(self.page_gov))
        self.style_nav_btn(btn_gov)
        layout.addWidget(btn_gov)

        btn_term = QPushButton("TERMINAL")
        btn_term.clicked.connect(lambda: self.content_stack.setCurrentWidget(self.page_terminal))
        self.style_nav_btn(btn_term)
        layout.addWidget(btn_term)
        
        layout.addStretch()
        
        # Live Clock
        self.lbl_time = QLabel("00:00:00")
        self.lbl_time.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.lbl_time)
        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)

        self.main_layout.addWidget(sidebar)

    def style_nav_btn(self, btn):
        btn.setStyleSheet(f"""
            QPushButton {{ 
                background-color: transparent; 
                color: #888; 
                border: none; 
                text-align: left; 
                padding: 15px; 
                font-size: 16px;
            }}
            QPushButton:hover {{ color: {FROST_BLUE}; background-color: #1a1a1a; }}
        """)

    def create_dashboard(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(40, 40, 40, 40)
        
        # Welcome Header
        lbl_welcome = QLabel("SYSTEM STATUS: ONLINE")
        lbl_welcome.setStyleSheet(f"font-size: 32px; color: {FROST_BLUE}; font-weight: bold;")
        layout.addWidget(lbl_welcome)
        
        # --- FINANCIAL MODULE ---
        fin_frame = QFrame()
        fin_frame.setStyleSheet("background-color: #1a1a1a; border-radius: 10px; padding: 20px; margin-top: 20px;")
        fin_layout = QVBoxLayout(fin_frame)
        
        lbl_fin_title = QLabel("OFF-CHAIN EXPENDITURES (USD)")
        lbl_fin_title.setStyleSheet("color: #888; font-size: 14px;")
        fin_layout.addWidget(lbl_fin_title)
        
        self.lbl_total_spent = QLabel("$0.00")
        self.lbl_total_spent.setStyleSheet(f"color: {FROST_RED}; font-size: 48px; font-weight: bold;")
        fin_layout.addWidget(self.lbl_total_spent)
        
        btn_refresh_fin = QPushButton("Sync Ledger")
        btn_refresh_fin.setStyleSheet(f"border: 1px solid #333; color: white; padding: 5px; width: 100px;")
        btn_refresh_fin.clicked.connect(self.update_financials)
        fin_layout.addWidget(btn_refresh_fin)
        
        layout.addWidget(fin_frame)
        layout.addStretch()
        return page

    def create_governance_view(self):
        # (Same as before - keeping it minimal for brevity)
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.addWidget(QLabel("GOVERNANCE MODULE"))
        self.lbl_gov_status = QLabel("Idle")
        layout.addWidget(self.lbl_gov_status)
        btn_check = QPushButton("Check Proposals")
        btn_check.clicked.connect(self.check_gov)
        layout.addWidget(btn_check)
        return page

    def create_terminal_view(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        term = QLabel(">_ TERMINAL ACTIVE")
        term.setStyleSheet("background-color: black; color: #0f0; padding: 20px;")
        layout.addWidget(term)
        return page

    # --- LOGIC ---
    def update_time(self):
        self.lbl_time.setText(datetime.datetime.now().strftime("%H:%M:%S"))

    def update_financials(self):
        """Reads the CSV and sums column 3 (Amount)"""
        total = 0.0
        if os.path.exists(LEDGER_FILE):
            try:
                with open(LEDGER_FILE, 'r') as f:
                    reader = csv.reader(f)
                    next(reader, None) # Skip header
                    for row in reader:
                        if len(row) > 3:
                            try:
                                total += float(row[3])
                            except ValueError:
                                pass
            except Exception as e:
                print(f"Ledger Error: {e}")
        
        self.lbl_total_spent.setText(f"${total:,.2f}")

    def check_gov(self):
        self.fetcher = DataFetcher()
        self.fetcher.data_ready.connect(lambda d: self.lbl_gov_status.setText(str(d)))
        self.fetcher.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FUI()
    window.show()
    sys.exit(app.exec())
