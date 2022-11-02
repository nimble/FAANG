def evalRPN(tokens):
    stack = []
    # 2 1 3
    # + *
    for token in tokens:
        if token not in ['*', '/', '+', '-']:
            # Stack will contain all numbers at this point.
            stack.append(int(token))
        else:
            a = stack.pop()
            b = stack.pop()
            if token == '+':
                stack.append(a+b)
            elif token == '-':
                stack.append(b-a)
            elif token == '*':
                stack.append(b*a)
            else:
                stack.append(int(b/a))
    # At the end we will be given the final result in the Stack.
    return stack.pop()
    
def main():
    tokens = ["2", "1", "+", "3", "*"]
    print(evalRPN(tokens))

if __name__ == '__main__':
    main()