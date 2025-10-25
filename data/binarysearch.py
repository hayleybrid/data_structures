# an array of boolean values is divided into two sections. the left section consists of all false, and the right section consist of all true. find the first true in a sorted boolean array of the right sections. 
# the index of the first true element, if there is no, return -1

def find_boundary(arr: list[bool]) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = (right + left) // 2
        if arr[mid]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index

if __name__ == "__main__":
        arr = [x == "true" for x in input().split()]
        result = find_boundary(arr)
        print(result)
        