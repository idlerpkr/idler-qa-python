import pytest

@pytest.fixture(scope="function")
def fixture_start_and_stop(request):
    print("\nHello i`m fist Alexandr fixture")
    l = []
    print("\nI create []")
    l.extend([777, 223, 3, 4, 5, 6, 7, 8])
    print("\nI add 8 numbers in  []")
    yield(l)
    def fin():
        print("\nBye glad to see u again")
    request.addfinalizer(fin)

@pytest.fixture(scope="function")
def function_fixture(request):
    print("\nHello i`m function fixture")
    a = 1000
    yield(a)
    def fin():
        print("\nBue i`m funtion fixture")
    request.addfinalizer(fin)

@pytest.fixture(scope="module")
def module_fixture(request):
    print("\nHello i`m module fixture")
    b = 300
    yield (b)
    def fin():
        print("\nBue i`m module fixture")
    request.addfinalizer(fin)



def test_one(fixture_start_and_stop):
    l = fixture_start_and_stop
    print("l -> ", l)
    assert len(l) == 8


def test_two(fixture_start_and_stop):
    l = fixture_start_and_stop
    print("l -> ", l)
    print("first element ->", l[0])
    ##Перевести весь список в int
    # for i in range(len(l)):
    #     old_value = l[i]
    #     new_value = int(old_value)
    #     l[i]=new_value

    a = l[0]
    b = l[1]
    summa = (a + b)
    #int(summa)
    print ("sum ->", summa)
    assert summa >= 999

def test_three(function_fixture,module_fixture):
    print ("\nHello i`m test")
    a = function_fixture
    b = module_fixture
    sum_A_B = a - b
    print ("\n Raznost ->", sum_A_B)
    assert sum_A_B == 700
