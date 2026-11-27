#Find the compound insterest for a given principal amount, rate of interest, and time period.
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (%): "))
time = float(input("Enter the time in years: "))

 
amount = principal * ((1 + rate / 100) ** time)

 
compound_interest = amount - principal

 
print(f"\nTotal Amount after {time} years: ${amount:.2f}")
print(f"Compound Interest earned: ${compound_interest:.2f}")
