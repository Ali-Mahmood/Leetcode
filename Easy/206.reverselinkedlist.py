# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        reversed = None

        while head:  # while head is not None
            next = head.next  # saving old heads next value
            head.next = reversed  # pointing head.next to reversed value which is initially None/Tail
            reversed = head  # set reversed to new value
            head = next  # iterate over next element in initial list

        return reversed
