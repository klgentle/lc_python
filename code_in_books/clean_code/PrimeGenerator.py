"""
 This class Generates prime numbers up to a user specified
 maximum. The algorithm used is the Sieve of Eratosthenes.
 Given an array of integers starting at 2:
 Find the first uncrossed integer, and cross out all its
 multiples. Repeat until there are no more multiples
 in the array.
"""


import math


class PrimeGenerator(object):
    def generatePrimes(self, maxValue: int) -> list:
        if maxValue < 2:
            return None
        else:
            self.__uncrossIntegersUpTo(maxValue)
            self.__crossOutMultiples()
            self.__putUncrossedIntegersIntoResult()
            return self.__result

    def __uncrossIntegersUpTo(self, maxValue: int):
        self.__crossedOut = [True, True]
        for i in range(2, maxValue+1):
            self.__crossedOut.append(False)
        #print(self.__crossedOut)

    def __crossOutMultiples(self):
        limit = self.__determineIterationLimit()
        for i in range(2, limit + 1):
            if self.__notCrossed(i):
                self.__crossOutMultiplesOf(i)

    def __determineIterationLimit(self):
        # Every multiple in the array has a prime factor that
        # is less than or equal to the root of the array size,
        # so we don't have to cross out multiples of numbers
        # larger than that root.
        iterationLimit = math.sqrt(len(self.__crossedOut))
        return int(iterationLimit)

    def __crossOutMultiplesOf(self, i: int):
        multiple = 2 * i
        while multiple < len(self.__crossedOut):
            self.__crossedOut[multiple] = True
            multiple += i

    def __notCrossed(self, i: int):
        return self.__crossedOut[i] == False

    def __putUncrossedIntegersIntoResult(self):
        self.__result = []
        for i in range(2, len(self.__crossedOut)):
            if self.__notCrossed(i):
                self.__result.append(i)

    def __numberOfUncrossedIntegers(self):
        count = 0
        for i in range(2, len(self.__crossedOut)):
            if self.__notCrossed(i):
                count += 1
        return count


if __name__ == "__main__":
    a = PrimeGenerator()
    expect = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
    assert(a.generatePrimes(90) == expect)
    print(a.generatePrimes(90))
