oupt = []
secondouot = []
listnum = int(input("How many elements you want to enter?\n"))
print("Enter {} elements".format(listnum))
for i in range (listnum):
    usdt = int(input())
    oupt.append(usdt)
for j in range((listnum - 1), -1, -1):
    secondouot.append(oupt[j])

print("Reverse list: {}".format(secondouot))