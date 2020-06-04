# Given an array of integers and an integer k,
# you need to find the total number of continuous subarrays whose sum equals to k.
#
# Example 1:
#
# Input:nums = [1,1,1], k = 2
# Output: 2
#
#
# Constraints:
#
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

# very good video explaining the concept: https://www.youtube.com/watch?v=bqN9yB0vF08


from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        subarrays = 0  # amount of subarrays = to k
        sums = defaultdict(int)  # create a dict which can create keys
        runningSum = 0  # the accumulative sum

        for num in nums:

            runningSum += num

            if runningSum == k:
                subarrays += 1
            if runningSum - k in sums:
                subarrays += sums[runningSum - k]  # get value of sums[runningSum - k] and add it to subarrays

            sums[runningSum] += 1
            # if key doesnt exist in sums it will create one and add the value 1
            # if key does exist it will add 1 to the value
        return subarrays


numlist = [1, 2, 3]
kval = 3

obj = Solution()

print(obj.subarraySum(numlist, kval))
