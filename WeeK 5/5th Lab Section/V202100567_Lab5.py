"""
VinUniversity
COMP1010 Introduction to Programming
Lab 05 - Week 5 - Strings and Testing
by Phan Tuan Khoi V202100567

Group: 1
Date: Oct 21, 2021

Disclaimer: I certify that this assignment is my own work and that I have not copied in part or whole or
otherwise plagiarised the work of other students and/or persons.
"""


"""
#--------------------------Problem 1--------------------------------
#  A basic if-else statement]
#-------------------------------------------------------------------
"""
goal = int(input("How many hours are you supposed to work? "))
current = int(input("How many hours have you worked this week? "))
work_time = abs(goal - current)
if current < goal:
    print("You must still work {} hours this week.".format(work_time))
else:
    print("You must take {} hours of vacation.".format(work_time))
"""
#--------------------------Problem 2--------------------------------
#  The if-elif-else statement
#-------------------------------------------------------------------
"""
score = int(input("What is your percentage in class? "))
if 100> score > 85:
    print("You got an A!")
elif 84>score>70:
    print("You got a B!")
elif 69>score>55:
    print("You got a C!")
elif 54>score>40:
    print("You got a D!")
elif 39>score>0:
    print("Sorry, you got a F.")
else:
    print("Enter a valid number")
"""
#--------------------------Problem 3--------------------------------
#  The if-else statement with boolean variables
#-------------------------------------------------------------------
"""
sat_score = int(input("What is your SAT score?"))
gpa_score = float(input("What is your GPA score?"))
if sat_score >= 1200 and gpa_score >= 3.5:
    print("Great, you qualify for the scholarship!")
else:
    print("Sorry, you don’t qualify for the scholarship")
"""
#--------------------------Problem 4--------------------------------
#  The nested if-else statement
#-------------------------------------------------------------------
"""
account_balance = 1000
user = input("""Welcome to VinUni Banking Service
                B: Account Balance
                D: Deposit
                W: Withdraw
                E: Exchange""")
option = (user.upper())
if option == "B":
    print("Your account_balance is {:,.2f}.".format(account_balance))
elif option == "D":
    deposit = int(input("Enter deposit amount: "))
    print("Your new account balance is ${:,.2f}".format(account_balance + deposit))
elif option == "W":
    withdrawal = int(input("Enter withdrawal amount: "))
    if withdrawal < account_balance:
        print("Your account balance after withdrawal is ${:,.2f}".format(account_balance - withdrawal))
    else:
        print("Insufficient Funds of - ${:,.2f}".format(abs(withdrawal - account_balance)))
        print("Your account balance is ${:,.2f}".format(account_balance))
elif option == "E":
    exchange = int(input("Enter exchange amount: "))
    if exchange < account_balance:
        print("The exchange of ${:.2f} in Vietnamese Dong is VND{:,.2f}".format(exchange, (exchange * 23175)))
        print("Your account balance: ${:,.2f}".format(account_balance - exchange))
    else:
        print("Insufficient Funds! Your available balance is ${:,.2f}".format(account_balance))
print("Thank you for using our service")
