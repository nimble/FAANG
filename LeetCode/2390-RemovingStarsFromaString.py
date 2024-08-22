class Solution:
    def removeStars(self, s: str) -> str:

        char_arr = list(s)

        stack = []
        for char in char_arr:
            if char != "*":
                stack.append(char)
            else:
                stack.pop()
        return ''.join(stack)
