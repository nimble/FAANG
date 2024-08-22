class Solution:
    def alternateDigitSum(self, n: int) -> int:
        # 431 (Positive -> Negative -> Positive)
        number = str(n)
        full_sum = 0
        is_pos = True
        for digit in number:
            if(is_pos):
                full_sum+=int(digit)
                is_pos = False
            else:
                full_sum-=int(digit)
                is_pos = True

        return full_sum
        
