import os
import zipfile
try:
    from google.colab import files
except ImportError:
    pass  # Handle non-Colab environments gracefully

def create_investor_package():
    print("[❄️] Generating Frost Protocol Investor Assets...")

    # --- 1. CREATE THE SLIDESHOW (HTML) ---
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Frost Protocol | Investor Deck</title>
        <style>
            body { background: #0D1117; color: white; font-family: sans-serif; overflow: hidden; }
            .slide { display: none; height: 100vh; padding: 40px; box-sizing: border-box; text-align: center; }
            .active { display: flex; flex-direction: column; justify-content: center; align-items: center; }
            h1 { color: #58A6FF; font-size: 3em; margin-bottom: 0.5em; }
            ul { text-align: left; display: inline-block; font-size: 1.5em; color: #C9D1D9; }
            li { margin-bottom: 15px; }
            .footer { position: fixed; bottom: 20px; width: 100%; text-align: center; color: #8B949E; }
            .controls { position: fixed; bottom: 50px; right: 50px; }
            button { background: #238636; color: white; border: none; padding: 15px 30px; font-size: 1.2em; cursor: pointer; border-radius: 6px; }
            button:hover { background: #2ea043; }
        </style>
    </head>
    <body>

    <div class="slide active" id="s1">
        <h1>❄️ THE FROST PROTOCOL</h1>
        <h2>The First Thermally-Adaptive Machine Economy</h2>
        <p>Jacob Frost | Founder</p>
    </div>

    <div class="slide" id="s2">
        <h1>THE PROBLEM</h1>
        <ul>
            <li><strong>Inefficient Compute:</strong> Devices waste heat.</li>
            <li><strong>Complex Web3:</strong> Wallets are too hard to use.</li>
            <li><strong>Dumb Hardware:</strong> Phones don't earn their keep.</li>
        </ul>
    </div>

    <div class="slide" id="s3">
        <h1>THE SOLUTION</h1>
        <ul>
            <li><strong>Finux OS:</strong> A custom, earning operating system.</li>
            <li><strong>FrostGlass:</strong> Augmented Reality interface.</li>
            <li><strong>Virgo Kernel:</strong> Turns heat into value.</li>
        </ul>
    </div>

    <div class="slide" id="s4">
        <h1>THE SECRET SAUCE</h1>
        <h2>Proof of Thermal Work (PoTW)</h2>
        <ul>
            <li>Dynamic Frequency Tuning (963Hz).</li>
            <li>Converts CPU heat into FNR Tokens.</li>
            <li>Deep Kernel Integration.</li>
        </ul>
    </div>

    <div class="slide" id="s5">
        <h1>FROSTGLASS AR</h1>
        <ul>
            <li>Heads-Up Wallet Display.</li>
            <li>Gesture-Based Signing.</li>
            <li>Spatial NFT Assets.</li>
        </ul>
    </div>

    <div class="slide" id="s6">
        <h1>TOKENOMICS (FNR)</h1>
        <ul>
            <li><strong>Total Supply:</strong> 100,000,000 (Fixed).</li>
            <li><strong>Genesis:</strong> 100% Locked in Cold Storage.</li>
            <li><strong>Utility:</strong> Gas, Licensing, Governance.</li>
        </ul>
    </div>

    <div class="slide" id="s7">
        <h1>TRACTION</h1>
        <ul>
            <li>✅ Genesis Block Mined.</li>
            <li>✅ Cold Storage Secured.</li>
            <li>🚀 "Iceland" Release: March 14, 2026.</li>
        </ul>
    </div>

    <div class="slide" id="s8">
        <h1>THE GOOGLE OPPORTUNITY</h1>
        <ul>
            <li>Native Android Integration.</li>
            <li>Data Sovereignty via Frostmind.</li>
            <li>The perfect Web3 answer for Mobile.</li>
        </ul>
    </div>

    <div class="slide" id="s9">
        <h1>THE TEAM</h1>
        <ul>
            <li><strong>Jacob Frost:</strong> Founder & Architect.</li>
            <li><strong>Kelsee Missler:</strong> Strategy.</li>
            <li><strong>Engineering:</strong> Ohio-Based Core Team.</li>
        </ul>
    </div>

    <div class="slide" id="s10">
        <h1>JOIN THE NETWORK</h1>
        <h2>Seeking Strategic Partnership</h2>
        <p>Contact: Jacob Frost</p>
    </div>

    <div class="footer">Slide <span id="pageNum">1</span> / 10</div>
    <div class="controls">
        <button onclick="nextSlide()">Next ></button>
    </div>

    <script>
        let current = 1;
        const total = 10;
        function nextSlide() {
            document.getElementById('s' + current).classList.remove('active');
            current++;
            if (current > total) current = 1;
            document.getElementById('s' + current).classList.add('active');
            document.getElementById('pageNum').innerText = current;
        }
        document.body.addEventListener('keydown', function(e) {
            if(e.key === 'ArrowRight' || e.key === 'Space') nextSlide();
        });
    </script>
    </body>
    </html>
    """

    with open("Frost_Pitch_Deck.html", "w") as f:
        f.write(html_content)

    # --- 2. CREATE THE WHITEPAPER (TXT) ---
    whitepaper_text = """
    THE FROST PROTOCOL WHITE PAPER v1.0
    -----------------------------------
    ABSTRACT
    The Frost Protocol introduces a unified ecosystem where the Operating System (Finux), 
    the User Interface (FrostGlass AR), and the Consensus Mechanism (Proof of Thermal Work) 
    are deeply integrated.

    (See full document in previous logs for complete text...)
    """
    
    with open("Frost_Whitepaper.txt", "w") as f:
        f.write(whitepaper_text)

    # --- 3. ZIP THEM ---
    zip_filename = "Frost_Investor_Package.zip"
    print(f"[...] Zipping files into {zip_filename}...")
    
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        zipf.write("Frost_Pitch_Deck.html")
        zipf.write("Frost_Whitepaper.txt")

    print(f"[✅] Package Created: {zip_filename}")
    
    # --- 4. TRIGGER DOWNLOAD (Colab Specific) ---
    if 'google.colab' in str(os.environ):
        print("[⬇️] Downloading to your device...")
        files.download(zip_filename)
    else:
        print(f"[i] File saved locally. You can find it at: {os.path.abspath(zip_filename)}")

if __name__ == "__main__":
    create_investor_package()
