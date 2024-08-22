# Valid Parentheses
def isValid(s):
    stack = []
    for i in s:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        elif i == ')' and len(stack) > 0 and stack[-1] == '(':
            stack.pop()
        elif i == '}' and len(stack) > 0 and stack[-1] == '{':
            stack.pop()
        elif i == ']' and len(stack) > 0 and stack[-1] == '[':
            stack.pop()
        else:
            return False
    return len(stack) == 0

def main():
    isValid()

if __name__ == '__main__':
    main()