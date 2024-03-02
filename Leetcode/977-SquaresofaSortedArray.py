class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sortedSquaresArray = []
        for num in nums:
            sortedSquaresArray.append(num ** 2)
        

        
        return sorted(sortedSquaresArray)
        
