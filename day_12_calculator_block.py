# Building The Automated Math Machine

def add_number(num1, num2):
    return num1 + num2

def multiply_number(num1, num2):
    return num1 * num2

# --- MAIN ENGINE CONTROL ---
print("--- Automated Math Machine Activated ---")

# Add two numbers together
sum_result = add_number(15, 25)

# Feed THAT result into the multiplier!
final_score = multiply_number(sum_result, 2)

print(f"15 + 25 = {sum_result}")
print(f"That result multiplied by 2 = {final_score}")