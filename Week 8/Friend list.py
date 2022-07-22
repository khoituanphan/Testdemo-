friend_list = []
while True:
    usip = input('Enter a name or "no friend" to end: ')
    usps = usip.lower()
    if usip == "":
        continue
    if usps != "no friend":
        friend_list.append(usip)
        while True:
            otin = input('Enter a name or "no more friend" to end: ')
            otinps = otin.lower()
            if otinps == "no more friend":
                print(friend_list)
                break
            else:
                friend_list.append(otin)
    else:
        print("Sorry, can I be your friend")
