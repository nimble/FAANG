class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if(len(word1) != len(word2)):
            return False
        
        # Build 2 Lists from Words
        word1_list = list(word1)
        word2_list = list(word2)

        # Let's count character occurences
        hashmap1 = {}
        for value in word1_list:
            hashmap1[value] = hashmap1.get(value, 0) + 1

        hashmap2 = {}
        for value in word2_list:
            hashmap2[value] = hashmap2.get(value, 0) + 1

        return sorted(hashmap1.values()) == sorted(hashmap2.values())

        
