import json
import time
import hashlib
from flask import jsonify

# --- FROST PROTOCOL: SMART CONTRACT REGISTRY ---
# The immutable addresses for the Frost Ecosystem
CONTRACTS = {
    "$FROST":    "0xc34a134b37e97e949a56461960d4cf5361ae832b",
    "FTC":       "0xee132a0fa1f0724d3ec3936f0cdc5213af748c42",
    "FROSTCOIN": "0x6a5c9062648db45b0ff92b8d9b86cd755452a571",
    "FNR":       "0xe3a50d4b636274b462f4be5f715a14a6a42e242d",  # <--- REWARD TOKEN
    "FETH":      "0xec9cf89a9829cc6d7aea06d5fc33ae23746076c8",
    "FsZT":      "0x815447cdcf1714b73d01db46955ee0e11195e63c",
    "OTHERS":    "0x52f260614c434ec3aefab821ae7b63e5272c5b36"
}

# --- CONFIGURATION ---
# Conversion: 1000 Game Points = 1.5 FNR
REWARD_TOKEN = "FNR"
CONVERSION_RATE = 0.0015 

# --- MOCK LEDGER (Simulating Google Firestore) ---
# In production, replace this dict with a connection to Firestore or SQL
user_ledger = {
    "JacobFrost": {"balance": 5000.00, "wallet": "0xJacobMainWallet"},
    "TestUser":   {"balance": 0.00,    "wallet": "0xTestWallet123"}
}

def sync_score(request):
    """
    The Google Cloud Function Entry Point.
    Receives Game Data -> Calculates FNR -> 'Mints' Tokens.
    """
    
    # 1. CORS Headers (Allows the Android App to talk to this Server)
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    headers = {'Access-Control-Allow-Origin': '*'}

    # 2. Parse Incoming Data
    request_json = request.get_json(silent=True)
    
    if not request_json or 'user_id' not in request_json or 'score' not in request_json:
        return (jsonify({"error": "Invalid Data Payload"}), 400, headers)

    user_id = request_json['user_id']
    game_score = int(request_json['score'])
    
    # 3. Calculate FNR Rewards
    tokens_earned = game_score * CONVERSION_RATE
    target_contract = CONTRACTS[REWARD_TOKEN]

    print(f"❄️ [FROST ORACLE] Incoming Sync: User {user_id} | Score {game_score}")
    print(f"❄️ [FROST ORACLE] Target Contract: {target_contract} ({REWARD_TOKEN})")

    # 4. Execute Smart Contract Interaction (Simulation)
    tx_hash = execute_mint_transaction(user_id, tokens_earned, target_contract)

    # 5. Update Internal Ledger
    if user_id not in user_ledger:
        user_ledger[user_id] = {"balance": 0.00, "wallet": "0xNewWallet"}
    
    user_ledger[user_id]['balance'] += tokens_earned
    new_balance = user_ledger[user_id]['balance']

    # 6. Response to App
    response_data = {
        "status": "success",
        "reward_token": REWARD_TOKEN,
        "contract": target_contract,
        "tokens_minted": tokens_earned,
        "new_balance": new_balance,
        "tx_hash": tx_hash,
        "message": f"Successfully mined {tokens_earned:.4f} {REWARD_TOKEN}"
    }

    return (jsonify(response_data), 200, headers)

def execute_mint_transaction(user_id, amount, contract_address):
    """
    Simulates the Web3 'mint' call to the specific Frost Protocol contract.
    """
    # In a live Web3 version, this is where we would use web3.py to sign a transaction
    # using the Owner Private Key and send it to the Polygon/ETH RPC.
    
    print(f"⛓️  [BLOCKCHAIN] Calling Smart Contract: {contract_address}")
    print(f"⛓️  [BLOCKCHAIN] Function: mint(to={user_id}, amount={amount})")
    
    # Simulate Network Latency
    time.sleep(0.5) 
    
    # Generate a fake Transaction Hash that looks like a real Ethereum Tx
    simulated_hash = "0x" + hashlib.sha256(f"{user_id}{amount}{time.time()}".encode()).hexdigest()
    
    print(f"✅ [BLOCKCHAIN] Transaction Confirmed: {simulated_hash}")
    return simulated_hash
import requests
import webbrowser
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import TwoLineAvatarIconListItem, ImageLeftWidget, IconRightWidget
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.clock import Clock

# --- CONFIGURATION ---
# Replace with your deployed Firebase URLs
FIREBASE_PROJECT_ID = "frost-crush"
GET_ITEMS_URL = f"https://us-central1-{FIREBASE_PROJECT_ID}.cloudfunctions.net/getStoreItems"
BUY_ITEM_URL = f"https://us-central1-{FIREBASE_PROJECT_ID}.cloudfunctions.net/buyItem"

# Links to your other APKs (Host these on GitHub Releases or Drive)
FROST_CRUSH_APK_URL = "https://github.com/JacobFrost/FrostCrush/releases/download/v1.0/frost_crush.apk"
GRAYSON_WALLET_APK_URL = "https://github.com/JacobFrost/GraysonsWallet/releases/download/v1.0/wallet.apk"

USER_ID = "JacobFrost" # This would be dynamic in a real login system

KV = '''
MDBoxLayout:
    orientation: 'vertical'

    MDTopAppBar:
        title: "FrostMart Ecosystem"
        elevation: 4
        md_bg_color: .2, .2, .2, 1

    MDBottomNavigation:
        panel_color: .2, .2, .2, 1
        selected_color_background: 0, 0, 1, .4
        text_color_active: 0, 1, 1, 1

        MDBottomNavigationItem:
            name: 'screen1'
            text: 'App Store'
            icon: 'google-play'

            MDScrollView:
                MDList:
                    id: app_list

        MDBottomNavigationItem:
            name: 'screen2'
            text: 'NFT Shop'
            icon: 'cart'
            on_tab_press: app.load_store_items()

            MDScrollView:
                MDList:
                    id: shop_list

        MDBottomNavigationItem:
            name: 'screen3'
            text: 'My Wallet'
            icon: 'wallet'

            MDBoxLayout:
                orientation: 'vertical'
                padding: "20dp"
                spacing: "20dp"
                
                MDLabel:
                    text: "FROST PROTOCOL"
                    halign: "center"
                    font_style: "H4"
                    theme_text_color: "Custom"
                    text_color: 0, 1, 1, 1
                
                MDLabel:
                    id: balance_label
                    text: "FNR Balance: Loading..."
                    halign: "center"
                    font_style: "H5"

                MDFillRoundFlatButton:
                    text: "Refresh Balance"
                    pos_hint: {"center_x": .5}
                    on_release: app.refresh_balance()
'''

class FrostMartApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        return Builder.load_string(KV)

    def on_start(self):
        # 1. Load the App Store List
        self.populate_app_store()
        self.refresh_balance()

    def populate_app_store(self):
        # Define the Ecosystem Apps
        apps = [
            {"name": "Frost Crush", "desc": "Play-to-Earn Match 3 Game", "url": FROST_CRUSH_APK_URL, "icon": "gamepad-variant"},
            {"name": "Grayson's Wallet", "desc": "Secure FNR & Crypto Storage", "url": GRAYSON_WALLET_APK_URL, "icon": "wallet-outline"},
            {"name": "Frost OS Launcher", "desc": "Custom Android Interface", "url": "http://google.com", "icon": "android"}
        ]
        
        list_view = self.root.ids.app_list
        list_view.clear_widgets()
        
        for app in apps:
            item = TwoLineAvatarIconListItem(text=app['name'], secondary_text=app['desc'])
            item.add_widget(ImageLeftWidget(icon=app['icon']))
            
            # Install Button
            btn = IconRightWidget(icon="download", on_release=lambda x, url=app['url']: webbrowser.open(url))
            item.add_widget(btn)
            list_view.add_widget(item)

    def load_store_items(self):
        # 2. Fetch Items from Firebase Cloud Function
        self.root.ids.shop_list.clear_widgets()
        try:
            # We use a thread or simple async request (blocking for simplicity here, use Thread in prod)
            req = requests.get(GET_ITEMS_URL)
            items = req.json().get('items', [])
            
            for i in items:
                item_row = TwoLineAvatarIconListItem(
                    text=f"{i['name']} ({i['cost_fnr']} FNR)",
                    secondary_text=i.get('description', 'No description')
                )
                item_row.add_widget(ImageLeftWidget(icon="cart-outline"))
                
                # Buy Button
                buy_btn = IconRightWidget(
                    icon="cash-plus", 
                    on_release=lambda x, i_id=i['id']: self.buy_item(i_id)
                )
                item_row.add_widget(buy_btn)
                self.root.ids.shop_list.add_widget(item_row)
                
        except Exception as e:
            print(f"Error loading store: {e}")

    def buy_item(self, item_id):
        # 3. Trigger Purchase via Cloud Function
        payload = {"user_id": USER_ID, "item_id": item_id}
        try:
            res = requests.post(BUY_ITEM_URL, json=payload)
            if res.status_code == 200:
                self.show_dialog("Purchase Successful!", "Item added to inventory.")
                self.refresh_balance()
            else:
                self.show_dialog("Purchase Failed", "Insufficient FNR or Network Error.")
        except:
            self.show_dialog("Error", "Could not connect to Frost Cloud.")

    def refresh_balance(self):
        # In a real app, fetch from Firebase user doc. Simulating for now:
        self.root.ids.balance_label.text = "FNR Balance: [Fetching...]"
        # You would add a get_balance cloud function or read from the sync response
        pass

    def show_dialog(self, title, text):
        self.dialog = MDDialog(title=title, text=text, buttons=[MDFillRoundFlatButton(text="OK", on_release=lambda x: self.dialog.dismiss())])
        self.dialog.open()

if __name__ == '__main__':
    FrostMartApp().run()
