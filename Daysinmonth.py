month = input('Enter the month : ')
mon = month[0:3].lower()
print(mon)
if mon == 'jan' or mon == 'may' or mon == 'mar' or mon == 'jul' or mon == 'aug' or mon == 'oct' or mon == 'dec':
    print(mon, "has 31 days")
elif mon == 'apr' or mon == 'jun' or mon == 'sep' or mon == 'nov':
    print(mon, 'has 30 days')
elif mon == 'feb':
    print(mon, 'has 28 days')
else:
    print(month, 'is Invalid Month')

