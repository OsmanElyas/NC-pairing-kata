def nc_max(numbers):
    if not numbers:
        return 0
    biggest = numbers[0]
    for number in numbers:
        if number > biggest:
            biggest=number
    return biggest


def nc_min(numbers):
    if not numbers:
        return 0
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest=number
    return smallest