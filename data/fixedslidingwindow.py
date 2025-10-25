#given an array (lis) nums consisted on only non-negative integers, find the largest sum among all subarrays of length k in nums
# if inpiut is nums = [1,2,3,7,4,1], k = 3, largest 3 is 3,7,4 sum is 14


def subarray_sum_fixed(nums: list[int], k: int) -> int:
    window_sum = 0
    for i in range(k):
        window_sum += nums[i]
    largest = window_sum
    for right in range(k, len(nums)):
        left = right - k
        window_sum -+ nums[left]
        window_sum += nums[right]
        largest = max(largest, window_sum)
    return largest

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    k = int(input())
    result = subarray_sum_fixed(nums, k)
    print(result)    