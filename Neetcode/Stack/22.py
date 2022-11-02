def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    res = []
    helper(n, n, '',res)
    return res 

def helper(left,right,s, res):
    if not right:
        res.append(s)
        return res
    if left:
        helper(left-1,right,s+'(',res)
    if right > left:
        helper(left,right-1,s+')',res)

def main():
    n = int(3)
    print(generateParenthesis(n))

if __name__ == '__main__':
    main()