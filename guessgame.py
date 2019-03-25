import random
ran = random.randint(1,10)
print("\t\t\t\t hiiiii....Welcome to Guessing Game...")
print("-"*80)
print("Enter Your Name to proceed....")
name = input()
i=1
print(f'WELCOME {name}')
while i<=5:
    num = int(input(f' Choose a number between 1 and 10 :'))
    if ran > num:
        print("Your guess is less than my guessed number")
    elif ran < num:
        print("Your Guessed number is greater than my guessed number")
    elif ran == num:
        print('Perfect..You won...')
        print('Guessed Number matches My guessed number.Guessed number is :',ran)
        break
    i+=1
else:
    print('Sorry..chances exceeded...you loose...')

