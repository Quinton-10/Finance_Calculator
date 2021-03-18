#Import math for math problems
import math
#Print user must choose investment or bond and print explenation of both
print("Choose either 'investment' or 'bond' from the menu below to proceed:")

print("\ninvestment     -to calculate the amount of interest you'll earn on interest.")
print("bond           -to calculate the amount you'll have to pay on a home loan.")

#User input investment or bond
finance=input("\nPlease enter your option 'investment' or 'bond': ")

#If user input is investment ask user to input amount of money the will invest, interest rate, years they are planning on investing and if they want simple or compouned interst
#If user input simple or compound use given formula and print total interest
#if user does not input valid input then print error message
if finance == "investment":
    deposit = int(input("\nPlease enter the amount of money you are depositing: "))
    rate= int(input("Please enter the iterest rate (as a persentage): "))
    years= int(input("Please enter the number of year you are planning on investing: "))
    interest=input("Please enter if you want simple or compound interest(enter 'simple' or 'compound'): ")
    rate= rate/100
    if interest == "simple":
        investment=round(deposit * (1 + rate * years),2)
        print(f"\nYour total interest is {investment}!")
    elif interest== "compound":
        investment=round(deposit * math.pow(1 + rate,years),2)
        print(f"\nYour total interest is {investment}!")
    else:
        print("\nERROR not a valid option")
        
#if user input "bond" ask user to input the value of their house, interest rate and total months the are going to repay
#use given formula to wokrout total interest repayment and print the total interest repayment amount
#if user input not valid print error message        
elif finance == "bond":
    value=int(input("\nPlease enter the present value of your house: "))
    rate=int(input("Please enter the interest rate: "))
    months=int(input("Please enter the number of months you plan on repaying the bond: "))
    rate= rate/12
    bond=round((rate*value)/(1 - (1+rate)**(-months)),2)
    print(f"\nYour total interest repayment on your bond is {bond}.")
else:
    print("\nERROR not a valid option")
    
    

