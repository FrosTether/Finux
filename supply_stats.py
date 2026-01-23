def calculate_projection(asset_name, initial_reward, max_supply, interval_blocks):
    print(f"\n--- {asset_name} Supply Projection (3M Block Intervals) ---")
    current_supply = 0
    reward = initial_reward
    
    # We simulate 10 halving cycles (approx 56 years)
    for era in range(10):
        era_total = reward * interval_blocks
        current_supply += era_total
        percent_of_max = (current_supply / max_supply) * 100
        
        print(f"Cycle {era} (Year {era * 5.67:.1f}): Reward: {reward:6.2f} | Total: {current_supply:12,.0f} | {percent_of_max:5.1f}% of Max")
        reward /= 2

# Projection Execution
calculate_projection("Kylecoin (KYLE)", 66.67, 400_000_000, 3_000_000)
calculate_projection("Frostnerjo (FNR)", 5.50, 33_000_000, 3_000_000)
