def sum_args(*args):
    if not args:
        return 0
    sum=0
    for number in args:
        sum = sum+number
    return sum