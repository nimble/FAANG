class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # Define our isPalindrome Fuction.
        def ispal(w):
            left, right = 0, len(w) - 1
            while left <= right:
                if(w[left] != w[right]):
                    return False
                right-=1
                left+=1
            return True

        for word in words:
            if ispal(word):
                return word
        return ""
        
