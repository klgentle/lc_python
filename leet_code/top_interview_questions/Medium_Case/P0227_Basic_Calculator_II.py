from pysnooper import snoop


class Solution:
    #@snoop()
    def calculate(self, s: str) -> int:
        s += '+0'
        stack, num, preOp = [], 0, "+"
        print(f"s:{s}")
        for i in range(len(s)):
            print(f"num:{num}")
            print(f"preOp:{preOp}")
            if s[i].isdigit(): 
                num = num * 10 + int(s[i])
            elif not s[i].isspace():
                if   preOp == "-":  
                    stack.append(-num)
                elif preOp == "+":  
                    stack.append(num)
                elif preOp == "*":  
                    stack.append(stack.pop() * num)
                else:               
                    stack.append(int(stack.pop() / num))
                preOp, num = s[i], 0
        return sum(stack)


if __name__ == "__main__":
    a = Solution()
    s = '1+2*3/4+6/6*8/9'
    a.calculate(s)
