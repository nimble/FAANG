class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        operations = 0
        left = 0
        right = len(nums) - 1
        while(left < right):
            if(nums[left] + nums[right] == k):
                operations+=1
                left+=1
                right-=1
            elif(nums[left] + nums[right] > k):
                right-=1
            else:
                left+=1
        
        return operations
        
