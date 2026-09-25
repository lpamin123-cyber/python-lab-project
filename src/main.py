# Week 2 Assignment: Simple Bill Calculator

print("--- Welcome to the Simple Bill Calculator ---")

# 1. Gather inputs from the user
subtotal = float(input("Enter the total food/bill amount ($): "))
tax_rate = float(input("Enter the tax rate (%): "))
tip_rate = float(input("Enter the tip percentage (%): "))
num_people = int(input("How many people are splitting the bill? "))

# 2. Perform calculations
tax_amount = subtotal * (tax_rate / 100)
tip_amount = subtotal * (tip_rate / 100)
total_bill = subtotal + tax_amount + tip_amount
amount_per_person = total_bill / num_people

# 3. Display formatted summary
print("\n--- Bill Summary ---")
print(f"Subtotal:         ${subtotal:.2f}")
print(f"Tax ({tax_rate}%):       ${tax_amount:.2f}")
print(f"Tip ({tip_rate}%):       ${tip_amount:.2f}")
print(f"Total Bill:       ${total_bill:.2f}")
print(f"Number of People: {num_people}")
print(f"Amount Per Person: ${amount_per_person:.2f}")
