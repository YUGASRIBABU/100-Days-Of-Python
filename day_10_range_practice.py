# Masternig Range and Numerical Limites
print("Range Function Power Test")
print("-" * 40)

print("Challenge 1: Count 1 to 5")
for i in range(1, 6):
    print(f"Count: {i}")

print("-" * 40)

print("Challenge 2: Skipping by 3s (Up to 15)")
# Starts at 3, stops before 16, jumps by 3 each time
for num in range(3, 16, 3):
    squared = num ** 2
    print(f"Number: {num} -> Squared: {squared}")

print("-" * 40)