'''
问题描述：
给定一个二叉树，判断它是否是合法的二叉查找树(BST)

一棵BST定义为：

节点的左子树中的值要严格小于该节点的值。
节点的右子树中的值要严格大于该节点的值。
左右子树也必须是二叉查找树。
一个节点的树也是二叉查找树。

示例：
输入：{2,1,4,#,#,3,5}
输出：true
解释：
	二叉树如下：
	  2
	 / \
	1   4
	   / \
	  3   5
这是二叉查找树。

思路：二叉树的中序遍历，如果是严格递增的，那么就是一颗二叉查找树

'''


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        # write your code here
        # 思路：二叉树的中序遍历，如果是严格递增的，那么就是一颗二叉查找树
        self.result = []
        self.traverse(root)
        for i in range(len(self.result) - 1):
            if self.result[i] < self.result[i + 1]:
                continue
            else:
                return False
        return True

    def traverse(self, root):
        if root:
            self.traverse(root.left)
            self.result.append(root.val)
            self.traverse(root.right)