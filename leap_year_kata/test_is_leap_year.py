from is_leap_year import is_leap_year

def test_divisible_by_four():
    assert is_leap_year(4) == True

def test_divisible_by_four_and_100():
    assert is_leap_year(900) == False

def test_divisible_by_all_three():
    assert is_leap_year(2000) == True

def test_normal_year():
    assert is_leap_year(2026) == False

def test_normal_year2():
    assert is_leap_year(2024) == True