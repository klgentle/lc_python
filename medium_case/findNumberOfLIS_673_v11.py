#! python3
from collections import Counter
from pprint import pprint
class Solution:
    def findNumberOfLIS(self, nums) -> int:
        # 给定一个未排序的整数数组，找到最长递增子序列的个数。
        '''
        to looking for increase sub set, conside each point of the list, 
        for each point create one increase list, if one element is large than it append it at end,
        if min than it then add it before.
        '''
        # questoins:
        # how to put element in the first position of one list? [1] + [2,3] = [1,2,3](lst = nums[i] + lst)

        # special cases1 (equal) [2,2,2]:
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        elif nums_len == 1:
            return 1
        if len(set(nums)) == 1:
            return nums_len
        # special case2 (decrease) [5,4,3,2,1] TODO

        num2 = [] 
        #num2 like [[],[],...,[]]
        # initialize
        for i in range(0,nums_len):
            num2.append([])

        # TODO num2 store index instead of value
        for j in range(0,nums_len):
            n2j = num2[j]
            n2j.append([])
            n2j[0].append(nums[j])
            #print('j: ', j)
            for k in range(0,len(n2j)):
                n2jk = num2[j][k]
                for i in range(0,nums_len):
                    if nums[i]<nums[j] and nums[i] < nums[n2jk[0]]:
                        n2jk = [i] + n2jk
                    elif nums[i]>nums[j] and nums[i] > nums[n2jk[-1]]:
                        n2jk.append(i)
                    elif nums[i] == nums[j]:
                        # copy the last element
                        n2j.append(n2j[-1])
                        n2j[-1].append(j)

        print('num2 _________________:')
        pprint(num2)

        # TODO mesure the least len, add one more for cycle
        target_len_list = [len(i) for i in num2]
        max_len = max(target_len_list)

        target_list_long = []
        for i in num2:
            if len(i) != max_len:
                continue
            if i not in target_list_long:
                target_list_long.append(i)

        print('target_list_long: ', target_list_long)
        print('ret: ', len(target_list_long))
        return len(target_list_long) 


if __name__ == '__main__':
    a = Solution()
    l = [1,1,1,2,2,2,3,3,3]
    a.findNumberOfLIS(l)
