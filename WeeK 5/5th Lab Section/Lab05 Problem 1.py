goal =    int(input("How many hours are you supposed to work? "))
current = int(input("How many hours have you worked this week? "))
work_time = abs(goal - current)
if current < goal:
    print("You must still work {} hours this week.".format(work_time))
else:
    print("You must take {} hours of vacation.".format(work_time))