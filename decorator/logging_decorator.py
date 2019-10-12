"""
TODO
write a decorator for logging out put 
"""

import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s"
)


def logging_begin_end(fn):
    def wrapper():
        logging.info("{0} begin ---------- ".format(fn.__name__))
        fn()
        logging.info("{0} end ----------".format(fn.__name__))

    return wrapper


@logging_begin_end
def test_logging_begin_end():
    print(111111111111)
    print(999999999999)


if __name__ == "__main__":
    test_logging_begin_end()
