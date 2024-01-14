class Solution:
    def reverseWords(self, s: str) -> str:
        words_arr = s.split(" ")
        reverse_string = ""
        N = len(words_arr)-1
        n = 0
        for word in words_arr[::-1]:
            if (n < N):
                reverse_string+=word + " "
            else:
                reverse_string+=word
            n+=1
        
        # Remove left & right spaces of the string
        reverse_string = reverse_string.lstrip(" ")
        reverse_string = reverse_string.rstrip(" ")
                
        # Now let's check for the extra spaces inbetween the words
        final_string = ""
        new_n = 0
        new_string = reverse_string.split(" ")
        for word in new_string:
            if(word != "" and new_n != len(new_string) - 1):
                final_string+=word + " "
            else:
                final_string+=word
            new_n+=1
        
        
        return final_string
