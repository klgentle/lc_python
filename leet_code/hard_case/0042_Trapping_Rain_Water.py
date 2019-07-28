#from pysnooper import snoop

class Solution:
    """
    part into three, every one use two pointer
    """
    #@snoop()
    def trap(self, height: list) -> int:
        left = 0
        right = len(height) -1
        water_trap_l = 0
        water_trap_r= 0
        water_trap_m = 0

        #@snoop()
        def sub_trap(height:list,left:int,right:int) -> tuple:
            left_out = left
            right_out = right
            min_heght = min(height[left],height[right])
            # height filter, change too high height to min height
            bar_height = sum(list(map(lambda x : x if x <= min_heght else min_heght, height[left+1:right]))) 
            water_trap_m = (right - left - 1) * min_heght  - bar_height
            
            # midum part
            while left < right:
                if height[left] <= height[right]:
                    left += 1
                else:
                    right -= 1

                min_heght = min(height[left],height[right])
                # height filter, change too high height to min height
                bar_height = sum(list(map(lambda x : x if x <= min_heght else min_heght, height[left+1:right]))) 
                water = (right - left - 1) * min_heght  - bar_height
                #water_trap_m = max(water_trap_m, water)
                if water > water_trap_m:
                    water_trap_m = water
                    left_out = left
                    right_out = right

            return (left_out, right_out, water_trap_m)
        
        left_m, right_m, water_trap_m = sub_trap(height, 0, right)
        left, right, water_trap_l = sub_trap(height, 0, left_m)
        left, right, water_trap_r = sub_trap(height, right_m, right)

        return max(water_trap_m,0) + max(water_trap_l,0) + max(water_trap_r,0)


if __name__ == "__main__":
    a = Solution()
    #h = [0,1,0,2,1,0,1,3,2,1,2,1] 
    h = [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]
    a.trap(h)
