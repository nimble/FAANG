class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr.sort()
        hashmap = {}
        for value in arr:
            hashmap[value] = hashmap.get(value,0) + 1
        
        # Now let's check the values to see if the occurences have appeared or not
        occurences = []
        for key, value in hashmap.items():
            if value not in occurences:
                occurences.append(value)
            else:
                return False
        return True




        
