class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        start_pointer = 0
        end_pointer = len(nums) - 1

        #   0  1  2
        # [ 3, 2, 4]

        #SP = 0
        #EP = 1

        while(start_pointer < end_pointer):
            current_sum = nums[start_pointer] + nums[end_pointer] # 7, #6
            if(current_sum == target):
                return start_pointer, end_pointer
            
            # Value not find, let's move left --
            end_pointer-=1
            # if start becomes neighbours with end_pointer, we want to move end back to end and move start an index up.
            current_sum = nums[start_pointer] + nums[end_pointer] # 7, #6
            if(current_sum == target):
                return start_pointer, end_pointer
                
            if(start_pointer+1 == end_pointer):
                start_pointer+=1
                end_pointer=len(nums)-1

