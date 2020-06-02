# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1]

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numIndex = {}

        for index, number in enumerate(nums):  # assigning an index to each number in nums using enumerate
            if target - number in numIndex:  # minus the number from the target and check if the remainder in numIndex
                return [numIndex[target - number], index]
            numIndex[number] = index  # add number to numIndex


solution = Solution()
print(solution.twoSum([2, 11, 7, 10], 9))

print(solution.twoSum([3, 3], 6))
