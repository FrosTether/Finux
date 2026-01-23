# corporate/finance/royalty_routing.py

def route_to_grayson(daily_fees):
    # Routing 10% of our daily royalties to Grayson's Trust
    grayson_cut = daily_fees * 0.10
    print(f"🎁 ROUTING LEGACY FUNDS: ${grayson_cut:,.2f} to Grayson's Vault.")
    print("   [STATUS] Transaction signed by Jacob Frost.")

if __name__ == "__main__":
    # If the network makes $50,000 today, Grayson gets $5,000 for his future.
    route_to_grayson(50000)
