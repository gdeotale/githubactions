from src.math_operations import add, sub

def test_add(a,b):
    assert add(2,3) == 5
    assert add(-2,3) == 1
    assert add(2,-3) == -1
    assert add(-2,-3) == -5

def test_sub(a,b):
    assert sub(2,3) == -1
    assert sub(-2,3) == -5
    assert sub(2,-3) == 5
    assert sub(-2,-3) == 1