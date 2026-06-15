# Day 9: Refactoring the Automated Age Challenge using For Loops
age_people = [12, 45, 66, 89]

print("Starting Day 9: Automated Age Processor (For Loop Edition)")
print("-" * 50)

# The For automatically loops throught the items and handles the logic
for current_age in age_people:

    # Check if the age is even or odd using modulo (%)
    if current_age % 2 == 0:
        final_age = current_age * 2   # Even
        print(f"Original Age: {current_age}")
        print(f"-> Even Number Detected! multiplying age by 2. Final: {final_age}")

    else:
        final_age = current_age + 5    # Odd
        print(f"Original Age: {current_age}")
        print(f"-> Odd Number Detected! Adding 5 to age. Final: {final_age}")

        print("-" * 50)
