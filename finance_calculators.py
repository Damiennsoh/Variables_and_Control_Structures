import math # importing a library

# Declaring variables for the loan calculation types with their respective values.
investment = "investment - to calculate the amount of interest you'll earn on your investment"
bond = "bond - to calculate the amount you'll have to pay on a home loan"
print(investment)
print(bond)

calculation_type_Choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower() # converts input to lowercase.
if calculation_type_Choice == "investment":
    deposit_amount = input("What amount are you depositing: ")
    print("Deposit amount is:", deposit_amount)
    interest_Rate = input("What interest rate do you want?: ")
    print("Interest rate is:", interest_Rate)

elif calculation_type_Choice == "bond":
    print("Felicia will be fucked by me one day")
elif len(calculation_type_Choice) < 1:
    print("You did not make a choice! please make a choice to proceed.")
elif calculation_type_Choice != "investment" and calculation_type_Choice != "bond":
    print("Invalid input! Enter the right options to proceed: ")


