ch = input('Enter a character :')
if ((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')) :
    print(ch ,'is a character')
elif (ch >= '0' and ch <= '9'):
    print(ch ,'is a number')
elif ch ==' ':
    print('Its a space')
else:
    print('its a special character')
