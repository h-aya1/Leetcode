# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-1)
        curr = dummy

        t1 = l1
        t2 = l2

        carry = 0

        while t1 != None or t2 != None:

            tot = carry

            tot += t1.val if t1 else 0
            tot += t2.val if t2 else 0

            l_sum = ListNode(tot % 10)
            carry = tot // 10

            curr.next = l_sum
            curr = curr.next

            t1 = t1.next if t1 else None
            t2 = t2.next if t2 else None

        if carry:

            l_sum = ListNode(carry)
            curr.next = l_sum
        
        return dummy.next
