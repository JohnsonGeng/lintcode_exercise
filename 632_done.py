'''
问题描述：在二叉树中寻找值最大的节点并返回。

示例：
输入:
{1,-5,3,1,2,-4,-5}
输出: 3
说明:
这棵树如下所示：
     1
   /   \
 -5     3
 / \   /  \
1   2 -4  -5

思路：任选一种遍历方式即可



'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:

    def maxNode(self, root):
        # write your code here
        # 任选一种遍历即可
        self.max_node = root
        self.preorderTraversal(root)
        return self.max_node

    def preorderTraversal(self, root):
        if root:
            if root.val > self.max_node.val:
                self.max_node = root
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
