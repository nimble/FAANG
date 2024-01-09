class Solution:
    def makeGood(self, s: str) -> str:
        # We will using a Stack for this.
        stack = []
        for char in s:
            # We're going to continue checking the stack to see if there's a similiar value already there. If there is, we will remove it. if not, add it to stack.
            if stack and char.swapcase() == stack[-1]:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)
                    

