"""
RemoveElementLC#26.py

LEETCODE #27
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

-Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
-Return k.

"""

global nums
def removeElement(nums, val):
        #left pointer for positioning
        left = 0
        # right for traversal
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left = left + 1
        return left

nums = [0,1,2,2,3,0,4,2]
val = 2
print('before nums', nums)
k = removeElement(nums, val)
print('after nums', nums[0:k])
print('length nums:', k)