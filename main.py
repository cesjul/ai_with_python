first_number = input('Insert a number: ')

while True:
    try:
        float_first_number = float(first_number)
        break
    except ValueError:
        first_number = input('Insert a number: ')
        if first_number.isdigit():
            float_first_number = float(first_number)
            break
        continue

operation = input('Insert a operation (* / + -): ')

while not operation in '- + / *':
    operation = input('Insert a operation (* / + -): ')

second_number = input('Insert a number: ')

while True:
    try:
        float_second_number = float(second_number)
        if second_number == '0' and '/' in operation:
                print('Cant divide by 0')
                print('Insert a new one')
                raise ZeroDivisionError
        break
    except ValueError:
        second_number = input('Insert a number: ')
        if second_number.isdigit():
            
            float_second_number = float(second_number)
            break
        continue
    except ZeroDivisionError:
        second_number = input('Insert a number: ')
        if second_number.isdigit() and second_number != '0':
            
            float_second_number = float(second_number)
            break



result = eval(f'{first_number}{operation}{second_number}')

print(result)
    

