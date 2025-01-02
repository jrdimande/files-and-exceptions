while True:
    try:
        num1 = int(input('Enter the firs number: '))
        num2 = int(input('Enter the second number: '))


    except ValueError:
        break
    else:
        sum = num1 + num2
        print(f'sum = {sum}')