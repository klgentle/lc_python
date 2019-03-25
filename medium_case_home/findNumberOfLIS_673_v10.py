#! python3
from collections import Counter
from pprint import pprint
class Solution:
    def findNumberOfLIS(self, nums) -> int:
    #def findNumberOfLIS(self, nums: List[int]) -> int:
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
            return len(nums)
        # special case2 (decrease) [5,4,3,2,1] TODO
        num2 = [] 
        #num2 like [[],[],...,[]]
        # initialize
        for i in range(0,len(nums)):
            num2.append([])
        for j in range(0,len(nums)):
            num2[j].append(nums[j])
            #print('j: ', j)
            # the before list
            for i in range(j-1,-1,-1):
                #print('i: ', i)
                #[1,3,5,4,7,...,5,8,9,100]
                if nums[i]<nums[j] and nums[i] < num2[j][0]:
                    num2[j] = [nums[i]] + num2[j]
            # the behead list
            for i in range(j+1,len(nums)):
                if nums[i]>nums[j] and nums[i] > num2[j][-1]:
                    num2[j].append(nums[i])
            #print('end i, num2: ', num2)
        print('num2 _________________:')
        pprint(num2)
        target_list = []
        for i in num2:
            if i not in target_list:
                target_list.append(i)
        print('target_list: ', target_list)
        target_len_list = [len(i) for i in target_list]
        max_len = max(target_len_list)
        count = Counter(target_len_list).most_common()
        
        # only on when duplicate value in the max_len sub then count duplicate times: TODO
        target_list_long = []
        for i in target_list:
            if len(i) == max_len:
                target_list_long.append(i)
        print('target_list_long: ', target_list_long)
        pop_list = []  # [i[0] for i in target_list_long]        
        # to deal with duplicate value
        """
        # get the index of dulplicate element, compare the response num2[i], 
        #if num2[i] is the same then add 1
        # [[1,2],[5,6,7]]
        # [(1,112),(4,112)]
        #dulp_list = []
        dulp_value_list = []
        nums_unique = []
        for e in nums:
            if e not in nums_unique:
                nums_unique.append(e)
            else:
                # filter the pop_list elements
                if e not in pop_list and e in target_list_long[0]:
                    dulp_value_list.append(e)
        dulp_value_list = list(set(dulp_value_list))
        print('dulp_value_list:', dulp_value_list)
        dulp_ind = []
        for i in dulp_value_list:
            sign_value_list = []
            for j in range(0,len(nums)):
                if nums[j] == i:
                    sign_value_list.append(j)
            print('sign_value_list: ', sign_value_list)
            dulp_ind.append(sign_value_list)
        print('dulp_ind: ', dulp_ind)
        for item in dulp_ind:
            print('item: ', item)
            for i in item:
                if num2[i] not in target_list_long:
                    continue
                for j in item:
                    print('num2[%s]:'%i, num2[i])
                    print('num2[%s]:'%j, num2[j])
                    #print('to_add:', to_add)
                    if i < j and num2[i] == num2[j]:
                        to_add +=1
        print('to_add:', to_add)
        target = dict(count).get(max_len)
        print('target: ', target)
        """
        # party 2 deal the continue dulplicate cases
        # target_list_long [[1,2,3],[1,2,3]]
        dul_nums = len(target_list_long)
        to_add = 0
        for item in target_list_long:
            for i in item:
                ind = nums.find(i)
                pass
            
        
        #return target+to_add

        
if __name__ == '__main__':
    a = Solution()
    l1 = [1,2,4,3,5,4,7,2]
    l2 = [1,1,1,2,2,2,3,3,3]
    a.findNumberOfLIS(l1)
