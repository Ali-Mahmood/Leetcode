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

        res: List[int] = []
        i: int = 0

        while i != target:
            for x in nums:
                for y in nums:
                    if x + y == target:
                        i += x + y
                        res.append(nums.index(x))
                        res.append(nums.index(y))
                        return res
                    else:
                        continue


solution = Solution()
print(solution.twoSum([2, 7, 11, 10], 9))
