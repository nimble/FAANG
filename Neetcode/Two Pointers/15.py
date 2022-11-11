def threeSum(nums):
    # [-1,0,1,2,-1,-4]
    # [[-1,-1,2],[-1,0,1]]
    new_arr = nums
    sums = []*3
    i = 0
    triplets = 0
    three_arrs = 0
    while(i!=0):
        if(checkZero(sum[three_arrs])!=0):
            sums[three_arrs].append(new_arr.remove(new_arr[i]))
            triplets +=1
        # no progress yet, just need commit.
    


def checkZero(nums):
    total_sum = sum(nums)
    return total_sum == 0

def main():
    threeSum([-1,0,1,2,-1,-4])


if __name__ == '__main__':
    main()