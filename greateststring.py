str1 = input('Enter string1 : ')
str2 = input('Enter String2 : ')
if ascii(str1) > ascii(str2):
    print(str1, 'is greatest')
elif ascii(str1) < ascii(str2):
    print(str2, 'is Greatest')
else:
    print('Both are same')
