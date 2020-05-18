from threading import Semaphore

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.sem = Semaphore()                   # default is 1
        self.sem3 = Semaphore(0)
        self.sem5 = Semaphore(0)
        self.sem15 = Semaphore(0)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        i = 3
        while i <= self.n:
            self.sem3.acquire()
            printFizz()
            i += 3
            if i % 5 == 0:
                i += 3
            self.sem.release()
    	

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        i = 5
        while i <= self.n:
            self.sem5.acquire()
            printBuzz()
            i += 5
            if i % 3 == 0:
                i += 5
            self.sem.release()
    	

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(15, self.n + 1, 15):
            self.sem15.acquire()
            printFizzBuzz()
            self.sem.release()
		

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.sem.acquire()
            if i % 15 == 0:
                self.sem15.release()
            elif i % 5 == 0:
                self.sem5.release()
            elif i % 3 == 0:   
                self.sem3.release()
            else:
                printNumber(i)     
                self.sem.release()
