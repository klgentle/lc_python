import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
import math
#value = math.factorial(x)
from pprint import pprint
class Solution:
    def distanceMeasure(self,list_a, list_b):
        # list_a, list_b like [1,0], [2,3] pairwise
        # 距离相等? which distance #math.sqrt
        dist = (list_a[0]-list_b[0])**2 + (list_a[1]-list_b[1])**2
        logging.debug('dist: %s' % dist)
        return dist
    def numberOfBoomerangs(self, points) -> int: # : List[List[int]]
        # points likes [[0,0],[1,0],[2,0]]
        points_len = len(points)
        tmp_list = []
        value_dict = {}
        ret = 0
        for i in range(0,points_len):
            logging.debug('points[%s]: %s' % (i,points[i]))
            print('value_dict: ',value_dict)
            print('tmp_list: ',tmp_list)    
            for j in range(0,points_len):
                if i == j :
                    continue
                dist = self.distanceMeasure(points[i],points[j])
                if dist not in tmp_list:
                    tmp_list.append(dist)
                else:
                    if dist not in value_dict:
                        value_dict[dist] = 2
                    else:
                        value_dict[dist] += 1
        for k,v in value_dict.items():
            print('v:', v)
            ret += v*(v-1)
        print('ret:', ret)
        return ret