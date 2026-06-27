# Function with Inputs and Outputs
print("--- Machine Calculation Processing ---")

# 1. We definr a machine that takes TWO parameters: base_price and tax_rate
def calculate_total_price(base_price, tax_rate):
    print(f"Processing item price: {base_price} with tax rate: {tax_rate}")

    total = base_price + (base_price * tax_rate)

    return total # This hands the final number back to whoever called it!

# 2. Call the function and STORE the returned result in a variable
final_bill = calculate_total_price(100, 0.05)

print(f"The main program received the returned total: ${final_bill}")
print("-" * 45)

# 3. We can reuse the same machine with different numbers instantly
sneaker_bill = calculate_total_price(250,0.08)
print(f"Sneaker final cost: ${sneaker_bill}")