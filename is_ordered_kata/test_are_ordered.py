from are_ordered import are_ordered

def test_empty_list():
    assert are_ordered([]) == False

def test_one_number():
    assert are_ordered([3]) == True

def test_two_numbers_in_order():
    assert are_ordered([2,5]) == True

def test_two_numbers_out_of_order():
    assert are_ordered([5,2]) == False

def test_two_of_the_same_number():
    assert are_ordered([5,5]) == True

def test_multiple_numbers_in_order():
    assert are_ordered([1, 2, 5, 8]) == True

def test_multiple_numbers_out_of_order():
    assert are_ordered([1, 2, 5, 8, 7, 3 ,1 , 9]) == False

def test_with_negative_numbers_in_order():
    assert are_ordered([[-8,-6,-3,-1, 2, 5, 8]]) == True

def test_with_negative_numbers_out_of_order():
    assert are_ordered([1,3,-3,5,-9,6]) == False

def test_floats_in_order():
    assert are_ordered([1.5,3.4,5.5,7.7]) == True

def test_floats_out_of_order():
    assert are_ordered([3.5, 1.1, 7.9, 9.0, 6.4]) == False
