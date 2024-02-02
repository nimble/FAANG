class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for digit in digits:
            s+=str(digit)
        
        num = int(s)+1
        digits = []
        for d in str(num):
            digits.append(int(d))

        return digits
        
