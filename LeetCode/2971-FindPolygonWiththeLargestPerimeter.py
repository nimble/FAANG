class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # 1,12,1,2,5,50,3
        # 1,1,2,3,5,12,50
        nums.sort()
        sum_val = 0
        largest_perimeter = -1
        # So essentially, we're going to keep a sum of all the left values that have passed. If we reach a value that is greater than our left, we're going to declare it as the largest perimeter
        # until we reach the very end of the array.
        for num in nums:
            if (num < sum_val):
                largest_perimeter = sum_val + total
            sum_val+=num
        return largest_perimeter
