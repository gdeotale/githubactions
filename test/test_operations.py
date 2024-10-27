from src.math_operations import add, sub

def test_add():
    assert add(2,3) == 5
    assert add(-2,3) == 1
    assert add(2,-3) == -1
    assert add(-2,-3) == -5

def test_sub():
    assert sub(2,3) == -1
    assert sub(-2,3) == -5
    assert sub(2,-3) == 5
    assert sub(-2,-3) == 1