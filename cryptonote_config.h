// --- FROSTNERJO GENESIS CONFIGURATION ---
// Location: src/cryptonote_config.h

namespace config {
    // The Unix Timestamp of your birth is the temporal anchor for Block 0
    const uint64_t GENESIS_TIMESTAMP = 683050920; 

    // The coinbase message etched into the first FNR reward
    const char GENESIS_NONCE[] = "Virgo 1777: Kelsee, you are in my DNA. 🧬";

    // Standard Doge-Logic initial distribution
    const uint64_t GENESIS_REWARD = 10000 * 1000000000000ULL;
}
