def add():
    sum = a+b
    print('The sum is:', sum)


def sub():
    dif = a-b
    print('The difference is:', dif)


def div():
    div = a/b
    print('The Division is:', div)


def mul():
    mul = a*b
    print('The multiplication is :', mul)


def mod():
    mod = a%b
    print('The modulus is', mod)


a = int(input('Enter number1 :'))
b = int(input('Enter number2 :'))
print(' 1.Addition \n 2.Subtraction \n 3.Division \n 4.Multiplication \n 5.Modulus \n 6.All Operations \n 7.exit')
ch = input('Enter Your Choice :')
if ch == '1':
    add()
elif ch == '2':
    sub()
elif ch == '3':
    div()
elif ch == '4':
    mul()
elif ch == '5':
    mod()
elif ch == '6':
    add()
    sub()
    div()
    mul()
    mod()
elif ch == '7':
    exit()
else:
    print('Invalid Option')

