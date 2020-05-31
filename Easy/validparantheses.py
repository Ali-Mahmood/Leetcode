# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

from typing import *


class Solution:
    def isValid(self, s: str) -> bool:

        stack: List[str] = []
        mapping = {
            '{': '}',
            '(': ')',
            '[': ']'
        }
        index: int = 0

        while index < len(s):
            bracket = s[index]
            if bracket == "(" or bracket == "{" or bracket == "[":
                stack.append(bracket)
            elif bracket == ")" or bracket == "}" or bracket == "]":
                if len(stack) == 0:
                    return False
                elif bracket == mapping.get(stack[-1]):  # gets stacks head value then gets value in mapping to match.
                    stack.pop()  # if it matches then remove it from the stack.
                else:
                    return False

            index += 1

        return len(stack) == 0


obj = Solution()

print(obj.isValid("({})"))
print(obj.isValid("(}{)"))
