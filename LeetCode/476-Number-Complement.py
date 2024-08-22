class Solution:
    def findComplement(self, num: int) -> int:
        # First, lets' convert the number to binary
        num_bin = bin(num)[2:]
        # we get 101 from this, now, let put it into a stack and then call bin on it again
        reversed_num = []
        frn = ''
        for n in num_bin:
            if(n == '1'):
                frn+=str(0)
            else:
                frn+=str(1)
        num = int(frn,2)
        return num
            
