str1 = input('Enter string1 : ')
str2 = input('Enter String2 : ')
if len(str1) > len(str2):
    print(str1, 'is Longest')
elif len(str1) < len(str2):
    print(str2, 'is Longest')
else:
    print('Both are same')
