class Solution:
    def findErrorNums(self, nums):
        the_dulp = []
        the_lost = []        
        max_num = len(nums)
        set_all = set(range(1,max_num+1))
        for i in set_all - set(nums):
            the_lost.append(i)
            break
        for i in nums:
            try:
                nums.remove(i)
                nums.remove(i)
            except ValueError:
                pass
            else:
                the_dulp.append(i) # is this not work? when?
        return the_dulp+the_lost

if '__name__' = '__main__':
    a = Solution()
    l = [33,86,39,20,22,99,75,1,31,58,35,13,48,66,80,82,94,14,50,93,43,63,98,95,8,70,44,68,74,17,59,36,5,23,7,69,3,21,30,92,78,73,77,54,47,42,40,34,64,11,51,4,57,15,16,28,12,29,62,4,91,18,83,45,38,56,2,84,27,6,41,61,88,52,71,90,67,79,76,24,37,96,19,97,53,26,87,49,9,85,32,72,10,89,55,46,81,65,60]
    a.findErrorNums(l)
    # questions: why the dulpicate 4 can not find? 