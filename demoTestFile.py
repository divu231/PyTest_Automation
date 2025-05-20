import pytest

def test_Demo1():
    a=4
    assert a==3, "test is failing"

@pytest.mark.smoke
def test_Demo2():
    a=4
    assert a==4


@pytest.mark.smoke
def test_Demo3():
    a=4
    assert a==4


@pytest.mark.regression
def test_empolyeedata():
    testdata ={
        "div":23,
        "dsd":53,
        "sdsd":43,
    }
    list2= []
    for x,y in testdata.items():
        if y>23:
            list2.append(y)
    
    assert list2==[53,43]