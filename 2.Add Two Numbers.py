# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i1 = 0
        i2 = 0
        n1 = 0
        n2 = 0
        while l1:
            n1 += l1.val * (10**i1)
            l1 = l1.next
            i1 += 1
        while l2:
            n2 += l2.val * (10**i2)
            l2 = l2.next
            i2 += 1
        added = [int(a) for a in list(str(n1+n2))[::-1]]
        head = ListNode(added[0])
        ans = head
        for i in range(1, len(added)):
            node = ListNode(added[i])
            head.next = node
            head = head.next
        return ans