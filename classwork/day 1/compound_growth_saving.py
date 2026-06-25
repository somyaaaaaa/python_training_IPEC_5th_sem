# Compound Growth of Savings

initial_amount = float(input("Enter Initial Amount: "))
years = int(input("Enter Number of Years: "))

final_amount = initial_amount * (2 ** years)

print("Final Amount =", final_amount)