# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        len_vals = len(vals)
        if len_vals < 2:
            return True
        elif vals[:int(len_vals)] == vals[int(len_vals)::-1]:
            return True
        else:
            return False