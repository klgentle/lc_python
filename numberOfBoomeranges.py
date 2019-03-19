import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
import math
#value = math.factorial(x)
from pprint import pprint

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        2 6 12    
        """
        def calDis(p1, p2):
            l1 = p1[0] - p2[0]
            l2 = p1[1] - p2[1]
            return l1 * l1 + l2 * l2

        l = len(points)
        if l < 3:
            return 0
        
        cnt = 0
        
        for i in range(l):
            distance = dict()
            for j in range(l):
                if j == i:
                    continue
                
                dis = calDis(points[i], points[j])
                
                if dis in distance:
                    distance[dis] += 1
                    num = distance[dis]
                    
                    if num == 2:
                        cnt += 2
                    else:
                        cnt += (num-1) * 2
                     
                else:
                    distance[dis] = 1
                    
        return cnt
