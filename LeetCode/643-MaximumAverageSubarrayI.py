class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = maxSum = sum(nums[:k])

        for i in range(k,len(nums)):

            currSum+=nums[i] - nums[i-k]

            maxSum = max(maxSum, currSum)
        
        return maxSum / k

        # while i < len(nums) - k + 1:
        #     window_sum = sum(nums[i:i+k]) / k 
        #     if window_sum > max_num:
        #         max_num = window_sum
        #     i += 1
        # return max_num
        
