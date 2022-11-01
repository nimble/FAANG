# Using AND 
def hammingweight(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def main():
    n = int(11)
    print(hammingweight(n))

if __name__ == '__main__':
    main()