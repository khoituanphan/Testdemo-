def progressive_tax(mon):
    ans = 0
    if mon > 2500:
        ans += 2500*5/100
        if mon > 5000:
            ans += (5000 - 2500) * 10 / 100
            if mon > 16500:
                ans += (16500 - 5000) * 18 / 100
                if mon > 41500:
                    ans += (41500 - 16500) * 28 / 100
                    ans += (mon - 41500) * 35 / 100
                else:
                    ans += (mon - 16500) * 28 / 100
            else:
                ans += (mon - 5000) * 18 / 100
        else:
            ans += (mon - 2500) * 10 / 100
    else:
        ans += mon * 5 / 100
    return ans

n = int(input("Enter Your Annual Income: "))
tax = progressive_tax(n)
print("Your tax due amount is: ${:,.2f}".format(tax))
print("Your effective tax rate is: {:.2f}%".format(tax/n*100))