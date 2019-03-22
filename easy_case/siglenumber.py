import logging
from pprint import pprint
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
class Solution:
    def isDul(self,i,nums):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                return True
        return False
    def singleNumber(self, nums) -> int:
        # if target in the last half: use index to find index != i
        # else if targe in the first half: find l[j] where l[i] = l[j] and i!= j continue 
        
        logging.debug('nums：%s ' % nums)
        #pprint(nums)
        nums_len = len(nums)
        logging.debug('nums_len：%s ' % nums_len)
        for i in range(0,nums_len):
            logging.debug('nums[%s]：%s'% (i,nums[i]))
            if self.isDul(i,nums):
                continue
            print('nums[i]; ', nums[i])
            return 