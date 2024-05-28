"""
RemoveDuplicatesLC#26.py

LEETCODE #26
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

-Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
-Return k.

-
References: https://youtu.be/DEJAZBq0FDA
"""
global nums
def removeDuplicates(nums):
    #left_ptr for positioning of unique values
    left_ptr = 1
    #right_ptr for traversal
    for right_ptr in range(1, len(nums)):
        if nums[right_ptr] != nums[right_ptr-1]:
            nums[left_ptr] = nums[right_ptr]
            #increment of left_ptr for next unique value positioning
            left_ptr += 1
    return left_ptr

nums = [1,1,2]
print('before nums', nums)
k = removeDuplicates(nums)
print('after nums', nums[0:k])
print('length nums:', k)