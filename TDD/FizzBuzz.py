class FizzBuzz(object):
    def __init__(self, num: int):
        self.num = num

    def fizz_buzz(self):
        if self.is_relat_to(3) and self.is_relat_to(5):
            return "FizzBuzz"
        elif self.is_relat_to(3):
            return "Fizz"
        elif self.is_relat_to(5):
            return "Buzz"
        else:
            return str(self.num)

    def is_relat_to(self, num2: int):
        if self.num % num2 == 0:
            return True
        else:
            return False
