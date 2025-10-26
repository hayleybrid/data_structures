#two sum
#given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 
#you may assume that each input would have exactly one solution, and you may not use the same element twice.

def two_sum(nums, target):
    num_to_index = {}                   
    for index, num in enumerate(nums):
        complement = target - num         
        if complement in num_to_index:   
            return [num_to_index[complement], index]  
        num_to_index[num] = index   
    return []  # return an empty list if no solution is found


if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    target = int(input())
    res = two_sum(nums, target)
    if res:
        print("Indices:", " ".join(map(str, res)))
    else:
        print("No solution found.")





