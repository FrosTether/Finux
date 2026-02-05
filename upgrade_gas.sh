cat << 'EOF' > upgrade_gas.sh
#!/data/data/com.termux/files/usr/bin/bash

echo "⚛️ PF GAS ENGINE — DEPLOYING"

mkdir -p www/system

cat << 'HTML' > www/system/gas.js
let balance = 0;
let gas = 1000;
let lastYield = 0;

function mintPF(){
  if(gas <= 0) return;
  gas -= 1;
  balance += simulate();
  render();
}

function shuffleGas(){
  if(gas < 10) return;
  gas -= 10;

  let best = 0;
  for(let i=0;i<100;i++){
    let sum = 0;
    for(let j=0;j<25;j++){
      sum += Math.random();
    }
    best = Math.max(best, sum);
  }
  lastYield = best;
  balance += best;
  render();
}

function simulate(){
  return Math.random() * 2;
}

function render(){
  document.getElementById("bal").innerText =
    "$" + (balance / 100).toFixed(2);
  document.getElementById("gas").innerText =
    "⛽ " + gas;
}
HTML

# Patch index.html safely
sed -i '/<\/script>/i \
<script src="system/gas.js"></script>' www/index.html

sed -i 's/mint()/mintPF()/g' www/index.html

sed -i '/actions/ a \
<button class="btn" onclick="shuffleGas()">shuffle ⛽ (PF)</button>\
<div class="label" id="gas">⛽ 1000</div>' www/index.html

echo "✅ PF GAS ENGINE ACTIVE"
echo "➡️  Shuffle now emits value"
EOF