'''
问题描述：

Given the root of a binary search tree (BST) and a value.

Return the node whose value equals the given value.

If such node doesn't exist, return null.

就是在二叉排序树中查找结点。

示例：
Input: value = 2
        4
       / \
      2   7
     / \
    1   3
Output: node 2

思路：
就是二叉排序树的查找
非递归：只要结点存在，并且结点的值和目标值不一样，就一直找下去


'''

class Solution:
    """
    @param root: the tree
    @param val: the val which should be find
    @return: the node
    """
    def searchBST(self, root, val):
        # Write your code here.
        # 思路：就是二叉排序树的查找
        # 非递归：只要结点存在，并且结点的值和目标值不一样，就一直找下去
        while root and val != root.val:
            if val < root.val:
                root = root.left
            else:
                root = root.right
        return root

