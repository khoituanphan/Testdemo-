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
