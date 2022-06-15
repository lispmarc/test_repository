## Contains the tests for the factorial
from test_package import factorial as fac

## Sucessfull tests
def test_1():
    assert fac.factorial(0)==1,"Base Case of factoris"

def test_2():
    assert fac.factorial(1)==1,"factorial of 1"

## UnsuccesFull tests (will be detected on github

def test_3():
    assert fac.factorial(3)==7,"(1) Causes a failure (although result is correct) must be corrected"
    
def test_4():
    assert fac.factorial(4)==25,"(2) Causes a failure (although result is correct) must be corrected"
    
def test_5():
    assert fac.factorial(2)==3,"(2) Causes a failure (although result is correct) must be corrected"
 