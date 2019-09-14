# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l = []
        if l1:
            while l1.next != None:
                l.append(l1.val)
                l1 = l1.next
            l.append(l1.val)
        if l2:
            while l2.next != None:
                l.append(l2.val)
                l2 = l2.next
            l.append(l2.val)
        
        if l:
            l.sort()
            head = ListNode(l.pop(0))
            ans = head
            for i in l:
                node = ListNode(i)
                head.next = node
                head = head.next
        else:
            ans = None
        return ans


    
