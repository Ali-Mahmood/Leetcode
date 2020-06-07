# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxDepth(self, root: TreeNode) -> int:
        result = []  # final list of lists
        if not root:  # if no root then return empty list
            return 0

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

        return len(result)

obj = Solution()

tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

print(obj.maxDepth(tree))
