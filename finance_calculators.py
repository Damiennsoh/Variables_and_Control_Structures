import math # importing a library

# Declaring variables for the loan calculation types with their respective values.
investment = "investment - to calculate the amount of interest you'll earn on your investment"
bond = "bond - to calculate the amount you'll have to pay on a home loan"
print(investment)
print(bond)

calculation_type_Choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower() # converts input to lowercase.
if calculation_type_Choice == "investment":
    deposit_amount = int(input("What amount are you depositing: ")) # int is placed in front of the  input before the parenthesis to convert any string into an integer
    print("Deposit amount is:", deposit_amount)
   
    interest_Rate = int(input("What interest rate do you want?: ")) 
    print("Interest rate is:", interest_Rate)
   
    investment_years = input("How many years do you plan on investing?: ")
    print("Investment years is:", investment_years)

# Declaring variables for both simple interest and compound interest and their respective formulas
simple_interest = (deposit_amount*interest_Rate*investment_years)*100
total_simple_interest_amount = deposit_amount + simple_interest # Adding the simple interest amount to the principal or initial amount invested

interest_type = input("Choose between simple interest or compound interest").lower() # Declaring a variable for type of interest
if interest_type == "simple":
    print("Simple interest =", simple_interest)
    print("Total amount=",total_simple_interest_amount )

elif calculation_type_Choice == "bond":
    print("Felicia will be fucked by me one day")
elif len(calculation_type_Choice) < 1:
    print("You did not make a choice! please make a choice to proceed.")
elif calculation_type_Choice != "investment" and calculation_type_Choice != "bond":
    print("Invalid input! Enter the right options to proceed: ")


