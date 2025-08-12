nums = [2, 3, 11, 15, 7]
target = 9

def two_sum(lst, target):
    my_dict = {}
    for i, num in enumerate(lst):
        complement = target - num
        if complement in my_dict:
            return [my_dict[complement], i]
        my_dict[num] = i
    return None  # If no solution

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

print(two_sum(nums, target))  # O(n) solution
print(twoSum(nums, target))   # O(n^2) solution
