class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest_candies = max(candies) 
        outputs = []
        for candie in candies:
            total_candies = candie + extraCandies
            if(total_candies >= greatest_candies):
                outputs.append(True)
            else:
                outputs.append(False)
        
        return outputs

        
