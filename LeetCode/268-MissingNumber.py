class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        uniqueNums = set()
        for num in nums:
            uniqueNums.add(num)
        uniqueNumsList = sorted(list(uniqueNums))
        i = uniqueNumsList[0]
        N = len(nums)
        for j in range(0,N):
            # print(uniqueNumsList[j])
            if(j != uniqueNumsList[j]):
                return j
            # We've reached end of array
            # print(j)
            if(j + 1 == N):
                return uniqueNumsList[-1] + 1

            
