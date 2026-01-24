const ethers = require('ethers');

// 1. Connection & Provider Setup
// Using a provider for the network your Frostcoin is deployed on (e.g., Ethereum Classic)
const provider = new ethers.JsonRpcProvider('YOUR_RPC_URL');

// 2. Wallet Setup (Your Private Key)
// WARNING: Keep your private key secure. Use environment variables in production.
const privateKey = 'YOUR_PRIVATE_KEY';
const wallet = new ethers.Wallet(privateKey, provider);

// 3. Contract Information
const tokenAddress = 'YOUR_FROSTCOIN_CONTRACT_ADDRESS';
const tokenAbi = [
  "function transfer(address to, uint256 amount) public returns (bool)"
];

const frostcoinContract = new ethers.Contract(tokenAddress, tokenAbi, wallet);

async function airdropFrostcoin() {
  const recipient = "0x024a622db08c69a17645473807aefe76ddc23560";
  
  // Set the amount (Assuming 18 decimals for FTC)
  const amount = ethers.parseUnits("20000", 18);

  console.log(`Initiating airdrop of 20,000 FTC to: ${recipient}...`);

  try {
    const tx = await frostcoinContract.transfer(recipient, amount);
    console.log(`Transaction sent! Hash: ${tx.hash}`);

    // Wait for the transaction to be mined
    await tx.wait();
    console.log("Airdrop successfully confirmed on the blockchain.");
  } catch (error) {
    console.error("Error during airdrop:", error);
  }
}

airdropFrostcoin();
