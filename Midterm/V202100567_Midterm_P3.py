def lunchPrice(item1, item2, day, month):
    global price
    price = item1 + item2
    if month[0] == 'M' or month[0] == 'J':
        if 'Thursday' in day:
            a = ((item2 / 100) * 10)
            item2 = (item2 - a)-5
        elif 'Friday' in day:
            a = ((item2 / 100) * 50)
            item2 = (item2 - a)-5
        else:
            price = price - 5
    else:
        if 'Thursday' in day:
            a = ((item2/100)*10)
            item2 = item2 - a
        elif 'Friday' in day:
            a = ((item2 / 100) * 50)
            item2 = item2 - a
        else:
            price = price
    return price

lunchPrice(8.5, 4.0, "Thursday", "August")

if price <0:
    price = 0
else:
    price = price
print(price)