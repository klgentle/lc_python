class Solution:
    def generateMatrix(self, n: int):
    #def generateMatrix(self, n: int) -> List[List[int]]:
        # TODO 递归
        # list.insert(index, obj)
        l = [[] for i in n]
        l[1] = list(range(1,n+1))
        l[-1] = list(range(3n-2,-1,2n-2))
        for i in range(n+1,2n-1):
            #ind = i-n
            l[i-n].insert(-1,i)
        for i in range(3n-2,4n-4+1):
            l[4n-3-i].insert(0,i)
        return [1] if n == 1 else return self.recursionMatrxi(n-1)

    def recursionMatrxi(self, n:int, lst):
        pass
        
 
 
