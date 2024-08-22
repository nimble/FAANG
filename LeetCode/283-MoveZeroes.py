class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for num in nums:
            if num == 0:
                to_back_val = nums.pop(nums.index(num))
                nums.append(to_back_val)
