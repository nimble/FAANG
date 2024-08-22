class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        while n != 1:
            result = 0
            str_num = str(n)
            for num in str_num:
                result += (int(num) ** 2)
            if result in visited:
                # if it's been visisted already.
                return False
            visited.add(result)
            # n will be updated now.
            n = result
        return True