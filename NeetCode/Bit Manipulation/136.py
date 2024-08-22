# Check what the outlier is in the list.
def single_number(arr):
    result = 0
    for i in arr:
        result = result ^ i
        print(result)
    return result


def main():
    #single_number([2,2,1])
    single_number([4,1,2,1,2])
if __name__ == '__main__':
    main()