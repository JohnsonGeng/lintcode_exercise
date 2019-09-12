'''
问题描述：在链表中插入一个节点。

示例：
输入：head = 1->4->6->8->null, val = 5
输出：1->4->5->6->8->null

思路：遍历链表即可，注意设置一个哑元结点，方便操作。

'''
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def insertNode(head, val):
    # write your code here
    # 遍历链表即可，注意设置一个哑元结点，方便操作。
    dummy = ListNode(-1, head)
    pre = dummy
    cur = dummy.next
    while cur:
        if val > cur.val:
            pre = pre.next
            cur = cur.next
        else:
            temp_node = ListNode(val, cur)
            pre.next = temp_node
            return dummy.next
    #有可能插入的元素刚好在最后一个，所以while循环结束需要生成结点插入链表
    temp_node = ListNode(val, cur)
    pre.next = temp_node
    return dummy.next