# Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

def two_sum(nums, target):
    current_index_num = {}
    
    for i, num in enumerate(nums):
        deff = target - num  # Calculate the difference needed to reach target
        
        # Check if the 'deff' is already in the dictionary
        if deff in current_index_num:
            return [current_index_num[deff], i]
        
        # Otherwise, store the current number's index in the dictionary
        current_index_num[num] = i


print(two_sum([2,7,11,15], 9)) # [0, 1]
print(two_sum([3,2,4], 6)) # [1, 2]
print(two_sum([3,3], 6)) # [0, 1]