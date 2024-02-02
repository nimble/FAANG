class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Split the words into an array
        words = s.split()
        # Start from the end of the array, if it's a valid value, we return it's length. 
        # Nice and simple solution :p
        for word in words[::-1]:
            if word:
                return len(word)
