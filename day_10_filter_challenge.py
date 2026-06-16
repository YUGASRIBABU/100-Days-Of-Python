# Data Filtering Coordination Challenge
print("Executing Batch Inventory Scan (IDs 10-50)...")
print("=" * 50)

# Step 1: Create a loop that runs from 10 up to and including 50
for tracking_id in range(10, 51):
    
    # Step 2: Rule 1 - Filter out numbers divisible by 10
    if tracking_id % 10 == 0:
        continue  # This skips the rest of the loop block and goes to the next ID
        
    # Step 3: Rule 2 - Check for Even numbers
    if tracking_id % 2 == 0:
        final_value = tracking_id * 2
        print(f"ID {tracking_id}: EVEN -> Final Value: {final_value}")
        
    # Step 4: Rule 3 - Handle Odd numbers
    else:
        final_value = tracking_id + 10
        print(f"ID {tracking_id}: ODD  -> Final Value: {final_value}")

print("=" * 50)
print("Batch Scan Complete!")