def searchMatrix(matrix, target):
    for l in matrix:
        if(target in l):
            for i, v in enumerate(l):
                if(v == target):
                    print(f"Found at index {i}")

def main():
    print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))


if __name__ == "__main__":
    main()