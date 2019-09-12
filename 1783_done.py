'''
问题描述：给出一棵二叉树，返回其节点值的后序遍历。

示例：
Input:{1,2,3}
Output:[3,2,1]

Explanation:
  1
 / \
2  3

思路：递归即可

需要实现非递归的版本，需要再刷！！！

'''


class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """

    def postorderTraversal(self, root):
        # write your code here
        self.result = []
        self.traversal(root)
        return self.result

    def traversal(self, root):
        if root:
            self.traversal(root.left)
            self.traversal(root.right)
            self.result.append(root.val)
