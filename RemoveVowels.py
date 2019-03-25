str = input("Enter a String:")
temp = ''
for i in str:
    if i not in 'aeiouAEIOU':
        temp = temp+i
print(f'After Removing Vowels String is :{temp}')