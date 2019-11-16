'''
问题描述：
Consider all the leaves of a binary tree.
From left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

示例1：
Input: {1,#,2,3}, {1,2,#,3}
Output:
Explaination:
the first tree:
  1
    \
     2
    /
   3
the second tree:
    1
   /
  2
 /
3
The leaf value sequence is: [3], so the same

示例2：
Input: {1,#,2,3}, {1,2,#,3}
Output:
Explaination:
the first tree:
  1
    \
     2
    /
   3
the second tree:
   1
  / \
 2   3
The first leaf value sequence is: [3], the second tree is: [2, 3], so it is not the same

思路：利用前序遍历的方式，只要是叶子结点，那么加入列表中。最后比较以下两个列表是否相等即可。

'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root1: the first tree
    @param root2: the second tree
    @return: returns whether the leaf sequence is the same
    """

    def leafSimilar(self, root1, root2):
        # write your code here.
        # 思路：利用前序遍历的方式，只要是叶子结点，那么加入列表中。
        # 最后比较以下两个列表是否相等即可。
        def getLeaves(root, result_list):
            if root:
                # 叶子结点
                if root.left is None and root.right is None:
                    result_list.append(root.val)
                getLeaves(root.left, result_list)
                getLeaves(root.right, result_list)

        result_list1 = []
        result_list2 = []
        getLeaves(root1, result_list1)
        getLeaves(root2, result_list2)
        return result_list1 == result_list2