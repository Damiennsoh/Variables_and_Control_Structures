import math # importing a library

# Declaring variables for the loan calculation types with their respective values.
investment = "investment - to calculate the amount of interest you'll earn on your investment"
bond = "bond - to calculate the amount you'll have to pay on a home loan"
print(investment)
print(bond)

# Initializing or declaring the following variables so that they can be accessed by 'if statements' of both scopes.
#  ie under both investment scope and the bond scope within their respective if statements.
deposit_amount = None # This means that under the choices of both investment and bond, I can use the variable 'deposit_amount' within the scope of their respective if statements.
interest_Rate = None
investment_years = None

calculation_type_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower() # converts input to lowercase.
if len(calculation_type_choice) < 1: # If no input is entered an error message will be displayed.
    print("You did not make a choice! please make a choice to proceed.")
elif calculation_type_choice != "investment" and calculation_type_choice != "bond": # If neither investment nor bond is entered, an error message will be displayed.
    print("Invalid input! Enter the right options to proceed: ")
elif calculation_type_choice == "investment":
    deposit_amount = int(input("What amount are you depositing: ")) # int is placed in front of the  input before the parenthesis to convert any string into an integer
    print("Deposit amount is:", deposit_amount)
   
    interest_rate = int(input("What interest rate do you want?: ")) 
    print("Interest rate is:", interest_rate)

    investment_years = int(input("How many years do you plan on investing?: "))
    print("Investment years is:", investment_years)

    simple_interest = (deposit_amount*interest_rate*investment_years)/100
    total_simple_interest_amount = deposit_amount + simple_interest # Adding the simple interest amount to the principal or initial amount invested
    
    interest_type = input("Choose between simple or compound: ").lower() # Declaring a variable for type of interest
    if interest_type == "simple":
       print("Simple interest =", simple_interest)
       print("Total amount=",total_simple_interest_amount )  
    elif interest_type != "simple" and interest_type != "compound": # Using an elif statement to create a condition so that if neither simple nor compound is entered, user is requested to enter the right input to continue
       print("Enter the right option to proceed: ")
    elif interest_type == "compound":
        compound__IR= interest_rate/100 # Where compound_IR = compound interest rate
        compound_interest = deposit_amount*math.pow((1+compound__IR), investment_years)
        print("The total amount if compound interest is applied is =", round(compound_interest, 2)) # round is used to convert the decimals into 2 decimal places

elif calculation_type_choice == "bond": # if user decides to chose bond, the below code under the elif block will execute
    present_value = int(input("Enter the present value of the house: "))
    print("The present value of the house =", present_value)

    interest_rate = int(input("What is your interest rate?: ")) # Asking for interest rate under bond calculation_type_choice
    print("The interest rate is =", interest_rate)

    number_months = int(input("Enter the number of months you will take to repay the bond: "))
    print("Number of months it will take to repay the bond is =", number_months)

    annual_IR = interest_rate/100 # since rates are in percentages, it means over 100
    monthly_IR = annual_IR/12 # since there are 12 months in a year
    monthly_repayments = (monthly_IR*present_value) / (1-(1+monthly_IR)**(-number_months)) # Formula for calculating bond repayments
    print("Amount user will have to repay each month =", monthly_repayments)
else:
    print("Start the whole process again")



