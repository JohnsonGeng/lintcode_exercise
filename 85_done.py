'''
问题描述：
给定一棵二叉查找树和一个新的树节点，将节点插入到树中。
你需要保证该树仍然是一棵二叉查找树。

示例：
样例 2:
	输入: tree = {2,1,4,3}, node = 6
	输出: {2,1,4,3,6}

	样例解释:
	如下：

	  2             2
	 / \           / \
	1   4   -->   1   4
	   /             / \
	  3             3   6

思路：找到插入位置即可。

'''

class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if root == None:    #找到了最终插入点
            return node
        else:               # 与当前结点比较，小的话去左子树查找，大的话去右子树查找
            if node.val < root.val:
                root.left = self.insertNode(root.left, node)
            else:
                root.right = self.insertNode(root.right, node)
        return root