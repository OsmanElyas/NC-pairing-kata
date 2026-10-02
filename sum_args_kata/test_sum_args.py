from sum_args import sum_args

def test_no_arg():
    assert sum_args()==0

def test_one_arg():
    assert sum_args(4) ==4

def test_two_positve_args():
    assert sum_args(5,7)==12

def test_two_neg_args():
    assert sum_args(-6,-11)==-17

def test_one_pos_one_neg_arg():
    assert sum_args(5,-1)==4

def test_float_args():
    assert sum_args(7.1, 9.2)== 7.1+9.2

def test_multiple_args():
    assert sum_args(5,8,1,2)==16