while True:
    password = input('Verify your password: ')

    if len(password) < 8:
        print('Your password is too short (8 char at least)')
        continue
    
    if not any(i.isdigit() for i in password):
        print('Your password must contain at least one number')
        continue
    
    if password.isdigit():
        print('Your password cannot be all numeric')
        continue

    print('Congrats, your password is strong')
    break