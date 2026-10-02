def are_ordered(numbers):
    if not numbers:
        return False

    
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            return False


    return True