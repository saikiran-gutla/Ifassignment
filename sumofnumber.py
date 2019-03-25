num = int(input("Enter a number:"))
sum = 0
# if num <= 9:
#     print(f'sum is :{num}')
# else:
while(num > 0):
    rem = num%10
    sum = sum+rem
    num//=10
print(f'sum of individual digits is {sum}')
