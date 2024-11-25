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



# Using Class object

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        num_to_index = {}
        
       
        for i, num in enumerate(nums):
            diff = target - num 
            
           
            if diff in num_to_index:
                return [num_to_index[diff], i]
            
    
            num_to_index[num] = i

solution = Solution()




nums1 = [2, 7, 11, 15]
target1 = 9
print(f"Test Case 1: {solution.twoSum(nums1, target1)}")  # Output: [0, 1]


nums2 = [3, 2, 4]
target2 = 6
print(f"Test Case 2: {solution.twoSum(nums2, target2)}")  # Output: [1, 2]


nums3 = [3, 3]
target3 = 6
print(f"Test Case 3: {solution.twoSum(nums3, target3)}")  # Output: [0, 1]
