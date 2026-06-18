# My First Custom Function (Light Session)
print("System Reboot: Day 11 Active")
print("-" * 30)

# 1. We DEFINE the custom machine named 'greet_user'
# It takes one input variable inside the parenthese: 'developer_name'
def greet_user(developer_name):
    print(f"Welcome back, Developer {developer_name}!")
    print ("Health bar restored. Ready to build step-by-step.")
    print("-" * 30)

# 2. We CALL (use) the machine and fed it a name string
greet_user("Yuga")
greet_user("Broo")