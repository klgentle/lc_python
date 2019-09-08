from timeit import Timer

def test_list_append():
    li = []
    for i in range(10000):
        li.append(i)
    return li

def test_list_add():
    li = []
    for i in range(10000):
        li += [i]
    return li
        
def test_list_derivation():
    return [i for i in range(10000)]
        
def test_list_function():
    return list(range(10000))


timer1 = Timer("test_list_append()", "from __main__ import test_list_append")
print("test_list_append:", timer1.timeit(1000))
timer1 = Timer("test_list_add()", "from __main__ import test_list_add")
print("test_list_add:", timer1.timeit(1000))
timer1 = Timer("test_list_derivation()", "from __main__ import test_list_derivation")
print("test_list_derivation:", timer1.timeit(1000))
timer1 = Timer("test_list_function()", "from __main__ import test_list_function")
print("test_list_function:", timer1.timeit(1000))