# Dynamic Receipt Generator Challenge

# This mashine takes an item and a price, and a output a perfectly aligned box line
def generate_receipt_line(item_name, price):
    # .ljust(15) aligns text to the left with in 15 spaces
    # .rjust(6) aligns tex to the right with in 6 spaces
    formattted_line = f"| {item_name.ljust(15)} : ${str(price).rjust(6)} |"
    return formattted_line

# --- MAIN ENGINE CONTROL (Like a cashier checkout system) ---
print("=============================================")
print("|             YUGA SUPERMARKET              |")
print("=============================================")

# Feeding real-world item data into our styling machine
line1 = generate_receipt_line("Coding keyboard", 49.99)
line2 = generate_receipt_line("Gaming Mouse", 25.50)
line3 = generate_receipt_line("Python Book", 19.00)

# Printing out the beautiful that our machine returned
print(line1)
print(line2)
print(line3)

print("====================================")