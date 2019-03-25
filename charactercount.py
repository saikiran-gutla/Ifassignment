str = input("Enter a String:")
ch = input("Enter a Character:")
cnt = 0
if ch in str:
    print("Character is found...")
    for i in str:
        if i == ch:
            cnt += 1
    print(f'{ch} character count is {cnt}')
else:
    print(f'{ch} is not found in {str}')
