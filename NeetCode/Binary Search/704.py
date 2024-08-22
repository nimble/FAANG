def search(nums,target):
    middle = len(nums) // 2
    i = 0
    # Search Right Hand Side
    if(target >= nums[middle]):
        while(middle != len(nums)):
            if(target == nums[middle]):
                return middle
            else:
                middle+=1
    else:
        while(i != middle):
            if(target == nums[i]):
                return i
            else:
                i+=1
    return -1



def main():
    print(search([-1,0,3,5,9,12], 2))


if __name__ == "__main__":
    main()
