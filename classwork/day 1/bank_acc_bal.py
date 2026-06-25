# taking input from the user
current_balance = float(input("Enter current balance: "))
withdrawal_amount = float(input("Enter withdrawal amount: "))

# Calculate remaining balance using arithmetic operator (-)
remaining_balance = current_balance - withdrawal_amount

# Output
print("Remaining Balance:", remaining_balance)