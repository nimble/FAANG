def twoSum(numbers, target: int):
    # [2,7,11,15]
    # 9
    found = False
    first_pointer = 0 
    last_pointer = len(numbers)-1
    while(first_pointer != last_pointer or found):
        if(numbers[first_pointer] + numbers[last_pointer] == target ):
            return first_pointer + 1, last_pointer + 1
        elif(numbers[first_pointer] + numbers[last_pointer] > target):
            last_pointer-=1
        else:
            first_pointer+=1
    

def main():
    print(twoSum([2,7,11,15], 9))


if __name__ == "__main__":
    main()