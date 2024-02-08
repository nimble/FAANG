class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique_num = 0
        for num in nums:
            unique_num ^= num
        return unique_num   

        # This solution is O(N) time complexity and O(N) space compelxity
        # hashmapuh = {}
        # for num in nums:
        #     hashmapuh[num] = hashmapuh.get(num,0) + 1
        # for key,value in hashmapuh.items():
        #     if(value == 1):
        #         return key
        
