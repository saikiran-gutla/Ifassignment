str = input("Enter a String:")
vowels = constant = special_char = digit = 0
li = []
for i in range(0,len(str)):
     ch = str[i]
     if((ch >= 'a' and ch <= 'z') or (ch >='A' and ch <='Z')):
         ch = ch.lower()
         if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
             vowels += 1
         else:
            constant += 1
     elif ch >= '0' and  ch <= '9':
            digit += 1
     else:
            special_char += 1
print(f'Vowels count :{vowels}')
print(f'Constants counts :{constant}')
print(f'Special Characters count :{special_char}')
print(f'Digits count :{digit}')
