cat << 'EOF' > manydays.sh
#!/data/data/com.termux/files/usr/bin/bash
set -e

STAMP=$(date +"%Y%m%d_%H%M%S")

echo "🖤 MANY DAYS IN — TERMUX RESET"
echo "Timestamp: $STAMP"

# Backup old www if exists
if [ -d "www" ]; then
  echo "📦 Backing up existing www → www_old_$STAMP"
  mv www www_old_$STAMP
fi

# Recreate structure
echo "📁 Creating fresh www/"
mkdir -p www/system www/assets

# Write index.html
echo "✍️ Writing vibe index.html"
cat << 'HTML' > www/index.html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>voluntaryistj.frostchain</title>

<style>
:root {
  --bg: #0b0b0d;
  --ink: #e6e6eb;
  --muted: #8a8a95;
  --accent: #b48cff;
}

* { box-sizing: border-box; }

html, body {
  margin: 0;
  padding: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: -apple-system, BlinkMacSystemFont, "Inter", system-ui, sans-serif;
  height: 100%;
}

body::before {
  content: "";
  position: fixed;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='120' height='120' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
  pointer-events: none;
}

.wrapper {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 40px 24px;
}

.header small {
  color: var(--muted);
  letter-spacing: 0.2em;
  font-size: 0.65rem;
}

.header h1 {
  font-weight: 500;
  font-size: 1.6rem;
  margin: 12px 0 60px;
}

.card {
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 18px;
  padding: 28px;
  margin-bottom: 24px;
}

.balance {
  font-size: 2.8rem;
  font-weight: 300;
}

.label {
  margin-top: 6px;
  font-size: 0.7rem;
  color: var(--muted);
  letter-spacing: 0.15em;
}

.actions {
  display: grid;
  gap: 14px;
}

.btn {
  padding: 16px;
  border-radius: 14px;
  background: transparent;
  border: 1px solid rgba(255,255,255,0.12);
  color: var(--ink);
  font-size: 0.9rem;
}

.footer {
  margin-top: 60px;
  font-size: 0.65rem;
  color: var(--muted);
  text-align: center;
  letter-spacing: 0.12em;
}
</style>
</head>

<body>
<div class="wrapper">

  <div class="header">
    <small>MANY DAYS IN</small>
    <h1>voluntaryistj.frostchain</h1>
  </div>

  <div class="card" onclick="mint()">
    <div class="balance" id="bal">$0.00</div>
    <div class="label">FROSTHASH</div>
  </div>

  <div class="actions">
    <button class="btn" onclick="shuffle()">shuffle / mulligan</button>
    <button class="btn" onclick="registry()">registry</button>
  </div>

  <div class="footer">
    built late • no rush • still here
  </div>

</div>

<script>
let bal = 0;
function mint(){ bal++; render(); }
function shuffle(){ if (bal > 0) bal--; render(); }
function registry(){ location.href = "system/registry.html"; }
function render(){
  document.getElementById("bal").innerText =
    "$" + (bal / 100).toFixed(2);
}
render();
</script>
</body>
</html>
HTML

echo "✅ Done."
echo "➡️  Next: surge www yourdomain.surge.sh"
EOF