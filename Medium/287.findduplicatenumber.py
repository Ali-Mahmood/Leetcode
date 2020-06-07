# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
# prove that at least one duplicate number must exist. Assume that there is only one duplicate number,
# find the duplicate one.
#
# Example 1:
#
# Input: [1,3,4,2,2]
# Output: 2
# Example 2:
#
# Input: [3,1,3,4,2]
# Output: 3
# Note:
#
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = nums[0]
        print(slow)
        fast = nums[slow]
        print(fast)

        while fast != slow:  # move slow pointer 1 step and fast pointer 2 steps until they collide
            slow = nums[slow]
            print(slow)
            fast = nums[nums[fast]]
            print(fast)
        fast = 0

        while fast != slow:  # restart fast from index 0 and move both pointers 1 step at a time
            slow = nums[slow]
            fast = nums[fast]
        return fast


obj = Solution()
print(obj.findDuplicate([1,2,3,3,4,5]))

# floyds tortoise and hare cycle detection
