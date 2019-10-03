# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        next = None
        while curr:
            next = curr.next
            
            curr.next = prev
            prev = curr
            curr = next
        return prev
        # if not head:
        #     return None
        # else:
        #     vals = [head.val]
        #     head = head.next
        #     while head:
        #         vals.append(head.val)
        #         head = head.next
        #     head_ = ListNode(vals[-1])
        #     ans = head_
        #     if not vals[:-1]:
        #         return ans
        #     else:
        #         for v in reversed(vals[:-1]):
        #             node = ListNode(v)
        #             head_.next = node
        #             head_ = head_.next
        #         return ans