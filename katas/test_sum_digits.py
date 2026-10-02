from sum_digits import sum_digits

def test_zero_returns_zero():
    assert sum_digits(0) == 0

def test_one_digit_input_returns_one_digit():
    assert sum_digits(1) == 1

def test_two_digit_input():
    assert sum_digits(44) == 8

def test_two_digit_input_ending_with_zero():
    assert sum_digits(10) == 1

def test_integer_represented_as_float_input():
    assert sum_digits(2.0) == 2

def test_float_input():
    assert sum_digits(2.7) == 9

def test_multiple_digits():
    assert sum_digits(464244) == 24

def test_example_1():
    assert sum_digits(99) == 18

def test_example_2():
    assert sum_digits(10.5) == 6

def test_multiple_zeros():
    assert sum_digits(10305070) == 16