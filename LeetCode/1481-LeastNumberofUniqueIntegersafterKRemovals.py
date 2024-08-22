class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        # Initalize Hashmap
        hashmap = {}
        for num in arr:
            # Count number of frequencys
            hashmap[num] = hashmap.get(num, 0) + 1
        
        # Sort the HashMap
        hashmap_sorted = dict(sorted(hashmap.items(), key=lambda item: item[1]))

        # Subtract k with the frequency
        for num, freq in hashmap_sorted.items():
            if k >= freq:
                k-=freq
                hashmap.pop(num)
            else:
                break

        return len(hashmap)
