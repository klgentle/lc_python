import time


def add_and_square(number: int):
    """求指定范围内所有满足 a*a + b*b = c*c 的a,b,c"""
    for a in range(0, number):
        for b in range(0, number):
            c = number - a - b
            if a**2 + b**2 == c**2:
                print(f"a : {a}, b: {b}, c:{c}")


if __name__ == "__main__":
    start_time = time.time()
    add_and_square(1000)
    print("time:",time.time()-start_time)
