# Design a class to find the kth largest element in a stream.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Your KthLargest class will have a constructor which accepts an integer k and an integer array nums,
# which contains initial elements from the stream. For each call to the method KthLargest.add,
# return the element representing the kth largest element in the stream.

from typing import *
import heapq


# kth largest refers to the item in the list which is the kth largest. For example if k = 2,
# you would want the 2nd largest item, if k = 10, you would want the 10th largest item
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)  # create a min heap our of the nums list in place
        while len(nums) > k:  # checks if the len of the list is larger then k
            heapq.heappop(nums) # pops smallest items off until length < k

        self.nums: List[int] = nums
        self.k: int = k

    def add(self, val: int) -> int:
        # if the val is equal to the smallest item or larger it doesnt change the result so its discarded
        # also the length of the heap must be equal to k for this to work
        if len(self.nums) == self.k and val <= self.nums[0]:
            return self.nums[0]

        heapq.heappush(self.nums, val)  # val is pushed onto the heap

        if len(self.nums) > self.k:  # if the size of the heap is larger then k once the val is added
            heapq.heappop(self.nums)  # then pop the smallest item of the heap
        return self.nums[0]  # returns head of the heap, as it is the kth largest


obj = KthLargest(3, [4, 5, 8, 2])

print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
