from max_and_min import nc_max, nc_min

def test_nc_max_empty_list_returns_zero():
    assert nc_max([])==0

def test_nc_min_empty_list_returns_zero():
    assert nc_min([])==0

def test_max_one_item_list_returns_item():
    assert nc_max([1]) == 1

def test_min_one_item_list_returns_item():
    assert nc_min([1]) == 1

def test_two_numbers_returns_min():
    assert nc_min([1,2]) == 1

def test_two_numbers_returns_max():
    assert nc_max([1,2]) == 2

def test_multiple_numbers_returns_min():
    assert nc_min([1,4,6,7,13]) ==1

def test_multiple_numbers_returns_max():
    assert nc_max([1,4,6,7,13]) ==13

def test_two_mins_returns_min():
    assert nc_min([1,1,5,7,8]) == 1

def test_two_max_returns_max():
    assert nc_max([1,1,5,7,8,8]) == 8

def test_negative_min():
    assert nc_min([-2, 0,6,8])==-2

def test_negative_max():
    assert nc_max([-2,-5,-8])==-2

def test_unordered_list_max():
    assert nc_max([8,1,4,1]) == 8

def test_unordered_list_min():
    assert nc_min([8,1,4,1]) == 1

def test_examples():
    assert nc_max([3, 7, 2, 9, 4])==9
    assert nc_min([3, 7, 2, 9, 4])== 2

def test_all_same_number_min():
    assert nc_min([3,3,3,3])==3

def test_all_same_number_max():
    assert nc_max([3,3,3,3])==3