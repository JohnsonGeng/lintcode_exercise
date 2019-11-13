'''
问题描述：
深度复制一个二叉树。

给定一个二叉树，返回一个他的克隆品 。

示例：
输入: {1,2,3,4,5}
输出: {1,2,3,4,5}
解释：
样例中二叉树如下所示:
     1
   /  \
  2    3
 / \
4   5

思路：


'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree
    @return: root of new tree
    """
    def cloneTree(self, root):
        # write your code here
        # 思路：任选一种遍历方式即可
        if root:
            # 如果结点不为空，那么生成一个结点就好了
            temp_node = TreeNode(root.val)
            temp_node.left = self.cloneTree(root.left)
            temp_node.right = self.cloneTree(root.right)
            return temp_node
        else:
            return None