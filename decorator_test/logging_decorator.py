"""
TODO
write a decorator for logging out put 
"""

import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s"
)


def logging_begin_end(fn):
    def wrapper(*args,**kwargs):
        logging.info("{0} begin ---------- ".format(fn.__name__))
        fn(*args,**kwargs)
        logging.info("{0} end ----------".format(fn.__name__))

    return wrapper


@logging_begin_end
def test_logging_begin_end(i:int):
    print(111111111111)
    print(f"-----------{i}-----------")
    print(999999999999)

def test_logging_begin_end2():
    print(222222222222)
    test_logging_begin_end()
    print(88888888888)



if __name__ == "__main__":
    test_logging_begin_end(100)
    #test_logging_begin_end2()
