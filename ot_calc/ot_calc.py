def week(d,p,t):
    hours = []
    for i in range(d):
        hour = input(f'enter number of hours worked on day {i+1}> ')
        try:
            float(hour)
        except ValueError:
            print(f'Please enter an integer. Quitting.')
        hours.append(float(hour))
    totalhours = sum(hours)
    if totalhours <= 40:
        totalpay = totalhours * float(pay)
    elif totalhours > 40:
        totalpay = (((totalhours-40)*1.5*float(pay)) + (40*float(pay))) * (float(t)/100)
    return totalpay

days1 = input(f'enter number of days worked in week 1> ')
days2 = input(f'enter number of days worked in week 2> ')
pay = input(f'enter pay rate> ')
tax = input(f'enter percentage of pay received after taxes (For example, enter 75 if you receive 75% of your check back after taxes)> ')
try:
    days1 = int(days1)
except:
    print(f'Please enter an integer. Quitting.')
    quit()
try:
    days2 = int(days2)
except:
    print(f'Please enter an integer. Quitting.')
    quit()
try:
    float(pay)
except:
    print(f'Please enter an integer or float. Quitting.')
    quit()
try:
    float(tax)
except:
    print(f'Please enter a valid number. Quitting.')
    quit()
print(f'Your total paycheck after taxes should be {round(week(days1,pay,tax) + week(days2,pay,tax),2)}.')