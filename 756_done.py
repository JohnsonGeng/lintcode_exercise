'''
问题描述：
给出两个链表形式表示的数字,写一个函数得到这两个链表相乘乘积。

示例：
输入：9->4->6->null,8->4->null
输出：79464
解释：946*84=79464

思路：非常简单，就是获取两个链表中数的值，还原成一个数，相乘即可

'''


def multiplyLists(l1, l2):
    # write your code here
    # 思路：非常简单，就是获取两个链表中数的值，还原成一个数，相乘即可
    l1_result = []
    l2_result = []
    p1 = l1
    p2 = l2
    sum1 = 0
    sum2 = 0
    counter1 = 0
    counter2 = 0
    while p1:
        l1_result.append(p1.val)
        p1 = p1.next
    while p2:
        l2_result.append(p2.val)
        p2 = p2.next
    i = len(l1_result) - 1
    j = len(l2_result) - 1
    while i >= 0:
        sum1 += l1_result[i] * (10 ** counter1)
        counter1 += 1
        i -= 1
    while j >= 0:
        sum2 += l2_result[j] * (10 ** counter2)
        counter2 += 1
        j -= 1
    return sum1 * sum2