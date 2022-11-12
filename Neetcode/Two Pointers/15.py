def threeSum(nums):

    sums = []*3
    eoa = len(nums) - 1
    print(eoa)
    three_arrs = 0
    i = 0
    # [-1,0,1,2,-1,-4]
    # [[-1,-1,2],[-1,0,1]]

    # [-1,] [ ] [ ]

    while(eoa!=0):
        if(checkZero(sums[three_arrs]) and len(sums[three_arrs]) !=0): # if equal to 0.
            # Move onto next Array.
            three_arrs+=1
        elif(sum(sums[three_arrs]) + nums[i] != 0 and len(sums[three_arrs]) != 0):
            sums[three_arrs].append(nums[i])
            i+=1
        eoa-=1
    
    return sums
    


def checkZero(nums):
    total_sum = sum(nums)
    return total_sum == 0

def main():
    print(threeSum([-1,0,1,2,-1,-4]))


if __name__ == '__main__':
    main()

