class Solution:
    def calculate(self, s: str) -> int:
        if s == '0':
            return 0
        s2 = s.replace(" ",'')
        if s2.isnumeric():
            return int(s2)
        out = 0
        length = len(s2)
        num_list = []
        method_list = []
        a = s2[0]
        # put all number and method in list
        for i in range(1,length):
            if s2[i].isnumeric():
                a += s2[i]
            else:
                a = int(a)
                num_list.append(a)
                a= ''
                method = s2[i]
                method_list.append(method)
                               
        # the last number to add
        a = int(a)
        num_list.append(a)
        print(f"num_list:{num_list}")
        print(f"method_list:{method_list}")
        
        mul = 1
        sum = 0
        method = method_list[0]
        # to deal with the first number
        if method in ('+','-'):
            out += num_list[0]            
            sum += num_list[0]
        elif method in ('*','/'):
            mul = num_list[0]
            out = sum + mul
        print(f"mul:{mul}")
        print(f"out:{out}")
        
        for j in range(len(method_list)):
            method = method_list[j]
            next_method = None
            if j != len(method_list) -1:
                next_method = method_list[j+1]
            num = num_list[j+1]
            if method == '+':
                if next_method in ('*','/'):
                    mul = num
                    sum = out
                else:
                    sum += num
                    out += num
            elif method == '-':
                if next_method in ('*','/'):
                    mul = -num
                    sum = out
                else:
                    sum -= num
                    out -= num
            elif method == '*':
                mul *= num
                out = sum + mul
            elif method == '/':
                mul = int(mul / num)
                out = sum + mul
        """
            print(f"mul:{mul}")
            print(f"sum:{sum}")
            print(f"out:{out}")
            
        print(f"mul:{mul}")
        """
        print(f"out:{out}")
        return out
