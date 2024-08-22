class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # bin_a = bin(int(a))[2:]
        # # print(bin_a)
        # bin_b = bin(int(b))[2:]

        # bin_c =  bin(int(bin_a,2) + int(bin_b,2))

        return bin(int(a, 2) + int(b, 2))[2:]
