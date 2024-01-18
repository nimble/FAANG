class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        SUM_TOTAL = sum(nums)
        SUM_LEFT = 0
        for idx, value in enumerate(nums):
            if(SUM_LEFT == SUM_TOTAL - SUM_LEFT - value):
                return idx
            SUM_LEFT+=value
        return -1
