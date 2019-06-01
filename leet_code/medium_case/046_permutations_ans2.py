import pysnooper

class Solution:
    @pysnooper.snoop()
    def permute(self, nums: list) -> list:
        save=[]
        stack=[]
        stack.append(([],nums))
        while stack:
            result,num=stack.pop()
            if num==[]:
                save.append(result)
                continue
            for i in range(len(num)):
                stack.append((result+[num[i]],num[:i]+num[i+1:]))
        return save


if __name__ == '__main__':
    a = Solution()
    a.permute([4,5,6,7,8])        
