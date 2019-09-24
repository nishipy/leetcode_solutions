# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        A = headA
        B = headB
        lenA = 0
        lenB = 0
        while headA != None:
            lenA += 1
            headA = headA.next

        while headB != None:
            lenB += 1
            headB = headB.next
        
        headA = A
        headB = B
        if lenA < lenB:
            diff = lenB - lenA
            for _ in range(diff):
                headB = headB.next
        else:
            diff = lenA - lenB
            for _ in range(diff):
                headA = headA.next
        
        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA