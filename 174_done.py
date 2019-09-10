'''
问题描述：给定一个链表，删除链表中倒数第n个节点，返回链表的头节点。
示例：
Example 1:
	Input: list = 1->2->3->4->5->null， n = 2
	Output: 1->2->3->5->null
思路：使用快慢指针，同时添加哑元结点，方便操作。

'''

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    # write your code here
    dummy = ListNode('#', head)
    if not head:
        return None
    slow = dummy
    fast = dummy
    for i in range(n + 1):
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next