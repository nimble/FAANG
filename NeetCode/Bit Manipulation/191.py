# Using AND 
def hammingWeight(self, n: int) -> int:
    one_bits = 0
    int_to_str = bin(n)
    for char in int_to_str:
        if(char == '1'):
            one_bits+=1
    return one_bits


def main():
    n = int(11)
    print(hammingweight(n))

if __name__ == '__main__':
    main()

# tEst