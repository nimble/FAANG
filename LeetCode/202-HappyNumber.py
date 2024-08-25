class Solution:
    def isHappy(self, n: int) -> bool:
        n_to_list = list(str(n))
        sum = 0
        while True:
            for num in n_to_list:
                sum += int(num) ** 2
            if(sum == 1):
                return True
            if(sum >=2 and sum <=9):
                if(sum == 7):
                    return True
                return False
            n_to_list = list(str(sum))
            sum = 0
        return True
