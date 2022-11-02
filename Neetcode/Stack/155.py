class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

        
    def push(self, val: int) -> None:
        self.stack.append(val)
        # If min stack doesn't have any value
        if not self.min:
            self.min.append(val)
        else:
            self.min.append(min(val, self.min[-1]))
        
    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()
        

    def top(self) -> int:
        if len(self.stack) != 0:
            return self.stack[-1]
        else:
            return None
        
    def getMin(self) -> int:
        return self.min[-1]