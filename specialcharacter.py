while True:
    ch = input("Enter a character :")
    if ch in '~`!@#$%^&*()_-=+][}{:/.,?><""':
        print(ch, 'is a special character')
    else:
        print('not a special character')
