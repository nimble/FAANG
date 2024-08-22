class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # First Solution
        pos_nums = []
        neg_nums = []
        for num in nums:
            if num >=0:
                pos_nums.append(num)
            else:
                neg_nums.append(num)
        
        final_arr = []
        for i in range(len(pos_nums)):
            final_arr.append(pos_nums[i])
            final_arr.append(neg_nums[i])

        return final_arr   

        # Second Solution    
        N = len(nums)
        p1 = 0
        p2 = 1
        res=[0]*N
        for num in nums:
            if num >= 0:
                res[p1] = num
                p1+=2
            else:
                res[p2] = num
                p2+=2

        return res
