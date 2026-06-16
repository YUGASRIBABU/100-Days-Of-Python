# Creative Terminal Dashboard Layout
dashboard_title = "SYSTEM TRACKING MATRIX"
items = ["System Status: ACTIVE", "Database Synchronization: 100%", "Security Protocols: ONLINE", "Total Connected Devices: 4"]

# Draw the top frame border
print("=" * 50)
print(f"| {dashboard_title.center(46)} |")
print("=" * 50)

# Loop through the data items and build dynamic walls
for item in items:
    # Use ljust to ensure the text content takes up exactly 44 spaces
    padded_content = item.ljust(44)
    print(f"|  [+] {padded_content} |")

# Draw the bottom frame border
print("=" * 50)