import sys
import psutil
import datetime
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QLabel, QFrame, 
                             QStackedWidget, QLineEdit, QMessageBox)
from PyQt6.QtCore import QTimer, Qt, QThread, pyqtSignal
from PyQt6.QtGui import QColor, QPalette

# Import the fixed tool
import governance_tool 

# --- THEME ---
FROST_BLUE = "#00e5ff"
FROST_DARK = "#121212"
FONT_MAIN = "Courier New"

# --- WORKER THREADS (Prevents UI Freezing) ---
class VoteWorker(QThread):
    finished = pyqtSignal(dict)
    
    def __init__(self, proposal_id, support):
        super().__init__()
        self.pid = proposal_id
        self.support = support

    def run(self):
        # This runs in background
        result = governance_tool.vote_on_blockchain(self.pid, self.support)
        self.finished.emit(result)

class DataFetcher(QThread):
    data_ready = pyqtSignal(dict)

    def run(self):
        data = governance_tool.get_latest_proposal()
        self.data_ready.emit(data)

# --- MAIN UI ---
class FUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FOME // Finux Operating Environment")
        self.setGeometry(100, 100, 1280, 720)
        self.apply_theme()
        
        # Layouts
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)
        
        # Sidebar
        self.create_sidebar()
        
        # Pages
        self.content_stack = QStackedWidget()
        self.main_layout.addWidget(self.content_stack)
        
        self.page_gov = self.create_governance_view()
        self.content_stack.addWidget(self.page_gov)
        
        # Auto-fetch data on load
        self.refresh_data()

    def apply_theme(self):
        self.setStyleSheet(f"background-color: {FROST_DARK}; color: white; font-family: '{FONT_MAIN}';")

    def create_sidebar(self):
        sidebar = QFrame()
        sidebar.setFixedWidth(200)
        sidebar.setStyleSheet("background-color: #0a0a0a; border-right: 1px solid #333;")
        layout = QVBoxLayout(sidebar)
        
        lbl = QLabel("FOME v1.0")
        lbl.setStyleSheet(f"color: {FROST_BLUE}; font-size: 20px; font-weight: bold;")
        layout.addWidget(lbl)
        
        btn_gov = QPushButton("GOVERNANCE")
        btn_gov.setStyleSheet(f"border: 1px solid {FROST_BLUE}; padding: 10px; color: {FROST_BLUE}")
        layout.addWidget(btn_gov)
        
        layout.addStretch()
        self.main_layout.addWidget(sidebar)

    def create_governance_view(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        
        layout.addWidget(QLabel("FROST PROTOCOL GOVERNANCE"))
        
        # Status Display
        self.lbl_status = QLabel("Loading data...")
        self.lbl_status.setStyleSheet("border: 1px solid #333; padding: 20px; font-size: 14px;")
        layout.addWidget(self.lbl_status)
        
        # Buttons
        btn_refresh = QPushButton("REFRESH DATA")
        btn_refresh.clicked.connect(self.refresh_data)
        layout.addWidget(btn_refresh)
        
        row_vote = QHBoxLayout()
        btn_yes = QPushButton("VOTE YES")
        btn_yes.clicked.connect(lambda: self.start_vote(True))
        btn_no = QPushButton("VOTE NO")
        btn_no.clicked.connect(lambda: self.start_vote(False))
        
        row_vote.addWidget(btn_yes)
        row_vote.addWidget(btn_no)
        layout.addLayout(row_vote)
        
        layout.addStretch()
        return page

    # --- LOGIC ---
    def refresh_data(self):
        self.lbl_status.setText("Fetching blockchain data...")
        self.fetcher = DataFetcher()
        self.fetcher.data_ready.connect(self.update_ui)
        self.fetcher.start()

    def update_ui(self, data):
        if "error" in data:
            self.lbl_status.setText(f"Connection Error:\n{data['error']}")
        else:
            text = (f"PROPOSAL #{data['id']}\n"
                    f"Topic: {data['desc']}\n"
                    f"----------------------\n"
                    f"✅ YES: {data['for']} FSC\n"
                    f"❌ NO:  {data['against']} FSC")
            self.lbl_status.setText(text)
            self.current_proposal_id = data['id']

    def start_vote(self, support):
        if not hasattr(self, 'current_proposal_id'):
            return
        
        self.lbl_status.setText("Broadcasting vote to Base Mainnet... (Please Wait)")
        
        # Run in background thread
        self.worker = VoteWorker(self.current_proposal_id, support)
        self.worker.finished.connect(self.vote_complete)
        self.worker.start()

    def vote_complete(self, result):
        if result["status"] == "success":
            QMessageBox.information(self, "Success", f"Vote Confirmed!\nTX: {result['hash']}")
            self.refresh_data()
        else:
            QMessageBox.critical(self, "Failed", f"Error: {result['message']}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FUI()
    window.show()
    sys.exit(app.exec())
