# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []  # final list of lists
        if not root:  # if no root then return empty list
            return result

        levelNodes = [root]  # root node as list

        while levelNodes:  # while this is not empty
            nextLevelsNodes = []  # set to empty to begin next level

            result.append([])  # append an empty list to result to append this levels node values

            for node in levelNodes:  # goes through each node on the same level
                result[-1].append(node.val)  # go to list/elem at tail position inside result and append node val
                if node.left:
                    nextLevelsNodes.append(node.left)  # append nodes in the next level left
                if node.right:
                    nextLevelsNodes.append(node.right)  # append nodes in the next level right

            levelNodes = nextLevelsNodes  # assign so that it iterates over the next levels nodes

        return result


obj = Solution()

tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

print(obj.levelOrder(tree))
