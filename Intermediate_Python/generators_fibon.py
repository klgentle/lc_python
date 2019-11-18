import time

def fibon(n):
    """
    计算斐波那契数列的生成器
    用这种方式，我们不用担心它会使用大量资源
    no return, no list
    """
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

    
def fibon_list(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result


if __name__ == "__main__":
    #start = time.time()
    #for x in fibon_list(100000):
    #    #print(x)
    #    pass
    #print(time.time() - start)

    start2 = time.time()
    for x in fibon(100000):
        print(x)
    print(time.time() - start2)
