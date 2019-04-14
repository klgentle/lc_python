class Solution:
    def plusOne(self, digits: list) -> list:
        l = len(digits)
        if digits[-1] < 9:
            digits[-1] += 1
        elif digits[-1] == 9:
            digits[-1] = 10
            for i in range(-1, -l, -1):
                #print(i)
                if digits[i] == 10:
                    digits[i] = 0
                    digits[i - 1] += 1
            if digits[0] == 10:
                digits = [1, 0] + digits[1:]
            print(f"digits:{digits}")
        return digits


if __name__ == "__main__":
    a = Solution()
    a.plusOne([8, 2, 1, 9, 9, 9])
