class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        merged_word = ""
        word1len = len(word1) - 1
        word2len = len(word2) - 1 

        total_iterations = word1len + word2len

        i = 0
        while(i <= total_iterations):
            # Let's first take word1's letter
            if(i <= word1len):
                merged_word+=word1[i]
            # Now let's add word2's letter
            if(i <= word2len):
                merged_word+=word2[i]
            
            i+=1

        return merged_word
