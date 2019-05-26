class Solution:
    def __init__(self):
        self.roman_dict = {
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            500: "D",
            400: "CD",
            900: "CM",
            1000: "M",
        }

    def intToRoman(self, num: int) -> str:
        if not 1 <= num <= 3999:
            return
        if num in self.roman_dict.keys():
            return self.roman_dict.get(num)
        ret = ""
        if num % 10 > 0:  # 8
            ret = self.fun(num, 1, ret)

        num = num // 10 * 10
        if num % 100 > 0:  # 50
            ret = self.fun(num, 10, ret)

        num = num // 100 * 100
        if num % 1000 > 0:  # 500
            ret = self.fun(num, 100, ret)

        num = num // 1000 * 1000
        if num % 10000 > 0:  # 5000
            ret = self.fun(num, 1000, ret)

        return ret

    def fun(self, num, min_d: int, ret: str) -> str:
        d = num % (min_d * 10)
        med = 5 * min_d
        if d in self.roman_dict.keys():
            ret = self.roman_dict.get(d) + ret
        else:
            if d > med:
                ret = (
                    self.roman_dict.get(med)
                    + self.roman_dict.get(min_d) * ((d - med) // min_d)
                    + ret
                )
            else:
                ret = self.roman_dict.get(min_d) * (d // min_d) + ret
        return ret
