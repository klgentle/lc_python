import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
class Solution:
    def findContentChildren(self, g, s) -> int: # : List[int]
        # sort the list, small cookie for small greed factor 
        g.sort()
        s.sort()
        logging.debug('g: %s' % g)
        logging.debug('s: %s' % s)
        child = 0
        cookie = 0
        cookie_amount = len(s)
        child_amount = len(g)
        while child < child_amount and cookie < cookie_amount:
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1
        return child