str = input('Enter a string')
rev = str[::-1]
print(rev, 'is reverse')
if str == rev:
    print(str, "is palindrome")
else:
    print(str, 'not palindrome')
