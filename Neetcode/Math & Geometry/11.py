class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l_pointer = 0 
        r_pointer = len(height) - 1
        max_area = 0
        while(l_pointer < r_pointer):
            area = (r_pointer - 1) * min(height[l_pointer],height[r_pointer])
            max_area = max(max_area,area)
            if(height[l_pointer] < height[r_pointer]):
                l_pointer+=1
            else:
                r_pointer-=1


        return max_area
