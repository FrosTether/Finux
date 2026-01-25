// --- FROSTNERJO MONOKILLER LOGIC ---
// Implements Doge-Style Even Distribution (10,000 FNR)
// Location: src/cryptonote_basic/cryptonote_basic_impl.cpp

bool get_block_reward(size_t median_weight, size_t current_block_weight, uint64_t already_generated_coins, uint64_t &reward, uint8_t version) {
    
    // Hard-coded fixed reward: 10,000 FNR
    // FNR uses 12 decimal places (atomic units)
    const uint64_t FIXED_REWARD = 10000 * 1000000000000ULL; 

    // Basic sanity check for block weight (standard protocol safety)
    if (current_block_weight > median_weight * 2) {
        return false;
    }

    // Apply the fixed reward regardless of 'already_generated_coins'
    // This removes the "scarcity" curve and enables even inflation.
    reward = FIXED_REWARD;

    // Penalty logic for oversized blocks (optional but recommended for network stability)
    if (current_block_weight > median_weight) {
        uint64_t penalty = FIXED_REWARD * (current_block_weight - median_weight) / median_weight;
        reward -= penalty;
    }

    return true;
}
