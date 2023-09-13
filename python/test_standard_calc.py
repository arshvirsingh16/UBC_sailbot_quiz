from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """


def test_bound_basic1():
    assert bound_to_180(0) == 0
def test_bound_basic2():
    assert bound_to_180(135) == 135
def test_bound_basic3():
    assert bound_to_180(-181) == 179
def test_bound_basic4():
    assert bound_to_180(700) == -20
def test_bound_basic5():
    assert bound_to_180(-700) == 20
 

""" Tests for is_angle_between() """


def test_between_basic1():
    assert is_angle_between(0, 1, 2) == True

def test_between_basic2():
    assert is_angle_between(15,90,150) == True

def test_between_basic3():
    assert is_angle_between(190,270,350) == True

def test_between1():
    assert is_angle_between(30,90,250) == False

def test_between2():
    assert is_angle_between(30,280,250) == True

def test_between3():
    assert is_angle_between(1,90,181) == True

def test_between4():
    assert is_angle_between(2,90,181) == True

def test_between5():
    assert is_angle_between(2,190,181) == False

def test_between6():
    assert is_angle_between(-15,90,179) == False

def test_between7():
    assert is_angle_between(-15,270,179) == True

def test_between8():
    assert is_angle_between(-15,90,110)== True

def test_between9():
    assert is_angle_between(2,90,190)== False

def test_between10():
    assert is_angle_between(2,270,190)== True




