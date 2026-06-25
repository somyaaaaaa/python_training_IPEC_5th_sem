#to find the simple interest
def simple_interest():
    p = float(input("Enter principal amount: "))
    r = float(input("Enter rate of interest: "))
    t = float(input("Enter time in years: "))
    si = (p * r * t) / 100
    return si

print("simple interest is:", simple_interest())
                        