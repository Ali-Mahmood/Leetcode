# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
#
#
# Note: You may assume the string contain only lowercase English letters.

from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:

        mapping = defaultdict(int)  # defaultdict allows keys to be added with a new value later

        for char in s:
            mapping[char] += 1  # add char in dict with count + 1 as it was in the string `s`.

        for index, char in enumerate(s):  # gets index and char in string `s`.
            if char in mapping and mapping[char] == 1:  # finds first occurring char with count/value set to 1.
                return index

        return -1


obj = Solution()
print(obj.firstUniqChar("loveleetcode"))
