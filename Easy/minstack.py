# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
#  
# Example 1:
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# Output
# [null,null,null,null,-3,null,0,-2]
#
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []  # the main stack
        self.min = []  # the stack containing the smallest item from the main stack, aka minimum stack

    def push(self, x: int) -> None:
        self.stack.append(x)

        if len(self.min) == 0 or self.min[-1] >= x:  # if the new item is the smallest then append it to the min stack
            self.min.append(x)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min[-1]:  # if the popped item is the smallest in the min stack then remove it
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]  # top of the main stack

    def getMin(self) -> int:
        return self.min[-1]  # top of the min stack, which is the smallest item


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
