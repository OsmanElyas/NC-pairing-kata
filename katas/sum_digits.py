
def sum_digits(number):
    tens = number// 10 
    unit = number % 10

    sum = 0
    num = str(number)

    for digit in num:
        if  digit != '.':
            sum = sum + int(digit)

    return sum