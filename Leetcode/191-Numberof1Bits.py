class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_form = bin(n)[2:]

        return binary_form.count('1')
        
