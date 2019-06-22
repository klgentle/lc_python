class Solution:
    def letterComb(self, ret: list, digits: str) -> List[str]:
        # 递归 每次取第一个数字代入，返回其余数字，进行递归。
        #print(f'ret:{ret}, digits:{digits}')
        if len(digits) == 0:
            return ret
        
        ret1 = []
        for i in ret:
            for k in self.dic.get(digits[0]):
                ret1.append(i+k)

        return self.letterComb(ret1,digits[1:])

    def letterCombinations(self, digits: str) -> List[str]:
        self.dic = {'2':['a','b','c'],
              '3':['d','e','f'],
              '4':['g','h','i'],
              '5':['j','k','l'],
              '6':['m','n','o'],
              '7':['p','q','r','s'],
              '8':['t','u','v'],
              '9':['w','x','y','z']}
        
        ret1 = []
        ret2 = []
        ret = []
        l = len(digits)
        if l == 0:
            return []
        elif l == 1:
            return self.dic.get(digits)
        elif l == 2:
            for i in self.dic.get(digits[0]):
                for j in self.dic.get(digits[1]):
                    ret.append(i+j)
            return ret
        else:
            for i in self.dic.get(digits[0]):
                for j in self.dic.get(digits[1]):
                    ret.append(i+j)
            return self.letterComb(ret,digits[2:])
        
