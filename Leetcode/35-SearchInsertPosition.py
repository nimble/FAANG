class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # we will set a left pointer and right pointer
        # [1,3,5,6]
        # 5
        left = 0 
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # let's first find where target may reside
            # resides on left
            if(target < nums[mid]):
                right = mid - 1
            elif(target > nums[mid]):
                left = mid + 1
            else:
                return mid
        
        return left
