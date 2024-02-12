class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        half_len = len(nums) / 2
        highest_val = 0
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        for k,v in hashmap.items():
            if v>= half_len:
                return k
                
        
