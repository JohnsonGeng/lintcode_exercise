'''
问题描述：
Given a non-empty, singly linked list with head node head,
return a middle node of linked list.
If there are two middle nodes, return the second middle node.

示例：
Example 1:

Input: 1->2->3->4->5->null
Output: 3->4->5->null

Example 2:

Input: 1->2->3->4->5->6->null
Output: 4->5->6->null

思路：先遍历一边链表得出链表长度，然后快指针先走链表长度的一半，慢指针再走。
当快指针走到最后结点的时候，慢指针刚好走到中间结点。

'''

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the head node
    @return: the middle node
    """
    def middleNode(self, head):
        # write your code here.
        # 思路：先遍历一边链表得出链表长度，然后快指针先走链表长度的一半，慢指针再走。
        # 当快指针走到最后结点的时候，慢指针刚好走到中间结点。
        list_length = 0
        p = head
        slow = head
        fast = head
        i = 0
        while p:
            list_length += 1
            p = p.next
        # 如果链表长度为奇数
        if list_length%2 == 1:
            list_length = int(list_length/2+1)
        else:
            list_length /= 2
        # 快指针先前进半个表长
        while i < list_length:
            i += 1
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow