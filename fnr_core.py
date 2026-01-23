def get_fnr_reward(height):
    interval = 3000000 # 5 years, 8 months
    halvings = height // interval
    return 5.50 / (2 ** halvings)
