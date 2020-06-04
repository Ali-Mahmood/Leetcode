# Given an array nums of n integers where n > 1,
# return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements of any prefix or
# suffix of the array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        products = [1]  # the product of all elements left of nums[0] is set to 1

        for i in range(1, len(nums)):
            products.append(nums[i-1] * products[-1])  # work out left product first

        rightProduct = 1  # the right side of the last value is set to 1

        for i in range(len(nums)-1, -1, -1):
            products[i] *= rightProduct  # working out right product by multiplying right result with left
            rightProduct *= nums[i]  # setting right product for num[i]

        return products


obj = Solution()

print(obj.productExceptSelf([1, 2, 3, 4]))
