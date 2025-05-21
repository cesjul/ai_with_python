def calc_tip(amount:float, porcent:float) -> float:
    '''
    porcent its a repr of X%. \r\n
    returns the proportional value based \r\n
    on amount and porcent recieved
    '''
    decimal_porcent = porcent / 100

    result = amount * decimal_porcent

    return result


amount = input('Type the amount: ')

tip_porcentage = input('Type the porcentage: ')

float_amount = 0
float_tip_porcentage = 0

if '.' in amount:
   if amount.replace('.', '').isdigit():
       float_amount = float(amount)
   else:
       print('Type a valid number')
else:
    print('The entry must have a float dot')

if '.' in tip_porcentage:
   if tip_porcentage.replace('.', '').isdigit():
       float_tip_porcentage = float(tip_porcentage)
   else:
       print('Type a valid number')
else:
    print('The entry must have a float dot')

print(calc_tip(float_amount, float_tip_porcentage))