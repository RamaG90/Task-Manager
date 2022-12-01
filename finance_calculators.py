# Capstone Project I - Financial Calculator

import math

# Financial Calculator is a program that allows the user access to two different financial calculators in order to calculate either the returns on an investment over a number of years or the monthly repayments on a home loan

# we begin by requesting the user to type in their investment choice: 'investment' or 'bond'

investment_type = input("Choose either 'investment' or 'bond' from the menu below to proceed:\n\ninvestment  -   to calculate the amount of interest you'll earn on your investment\nbond        -   to calculate the amount you'll have to pay on a home loan\n\nType in your selection: " )
print()

# using an if statement, we accept lower case, upper case or capitalized input for the user selection so the program is not affected
# we print out a message informing the user of their selection

if investment_type == "investment" or investment_type == "investment".upper() or investment_type == "investment".capitalize():
    print("You have selected 'investment'")
    print()

    # if the user selects 'investment', we proceed to request the following inputs from the user: the amount of money they will invest, the interest rate, the length of the investment in years and the desired method of interest rate calculation to calculate their returns

    deposit = float(input("Enter the amount of money deposited (in US$): "))
    print()
    rate = float(input("Enter the yearly interest rate (in %): "))
    print()
    time = int(input("Enter the number of years you plan to keep your money in: "))
    print()
    method = input("Please type 'simple' or 'compound' to select the interest method used to calculate your returns: ")
    print()

    # the program then calculates the investment returns using the formulas provided based on the user's chosen interest method (simple or compound)
    # we print a message to the user stating the return and the values selected for the variables above

    if method == "simple":
        return_simple = deposit * ((1 + (rate / 100) * time))
        print(f"Your return will be US${round(return_simple, 2)}, using {method} interest for an investment of US${deposit} during {time} years at a yearly rate of {rate}%.")
    elif method == "compound":
        return_compound = deposit * math.pow((1 + (rate / 100)), time)
        print(f"Your return will be US${round(return_compound, 2)}, using {method} interest for an investment of US${deposit} during {time} years at a yearly interest rate of {rate}%.")

elif investment_type == "bond" or investment_type == "bond".upper() or investment_type == "bond".capitalize():
    print("You have selected 'bond'")
    print()
    
    # if the user selects 'bond', we proceed to request the following inputs from the user: the value of their house, the yearly interest rate and how long they plan to take to repay the bond in months

    house_value = float(input("Enter the present value of your house (in US$): "))
    print()
    rate = float(input("Enter the yearly interest rate (in %): "))
    print()
    time = int(input("Enter in how many months you plan to repay the bond: "))
    print()

    # program calculates the monthly payments the user will have to make to until the loan is repaid
    # we print out a message to the user with this information

    monthly_payments = ((rate/12/100) * house_value) / (1 - ((1 + rate) ** (-time)))
    print(f"Your monthly payments will be US${round(monthly_payments, 2)} during {time} months until the loan is fully repaid, for a house valued at US${house_value} at a yearly interest rate of {rate}%.")

# if the user inputs anything else, we prompt and error message and request the user to retry.

else:
    print("Your input is incorrect. Please try again.")
    print()
