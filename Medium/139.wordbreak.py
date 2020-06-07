# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
# # determine if s can be segmented into a space-separated sequence of one or more dictionary words.
# #
# # Note:
# #
# # The same word in the dictionary may be reused multiple times in the segmentation.
# # You may assume the dictionary does not contain duplicate words.
# # Example 1:
# #
# # Input: s = "leetcode", wordDict = ["leet", "code"]
# # Output: true
# # Explanation: Return true because "leetcode" can be segmented as "leet code".

# time and space complexity: O(n**3) and O(n)

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        canMake = [False] * (len(s)+1)  # creates list of False for every item char in str
        canMake[0] = True  # sets position 1 to true

        for i in range(1, len(s)+1):
            for j in range(i-1, -1, -1):
                if canMake[j] and s[j:i] in wordDict:
                    print(j)
                    print(i)
                    print(s[j:i])
                    canMake[i] = True
                    break
        return canMake[-1]


obj = Solution()
print(obj.wordBreak("leetcode", ["leet", "code"]))
